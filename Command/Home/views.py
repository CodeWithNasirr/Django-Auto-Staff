from django.contrib import messages
from django.shortcuts import render,redirect
from .utils import get_all_models
from django.core.management import call_command,CommandError
from django.db import transaction
from django.core.mail import send_mail
from Upload.models import upload
from Home.task import import_data_task ,export_data_task
from Home.utils import check_csv_error
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def Register(request):
    if request.method =="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        pass2=request.POST.get('Confirm-password')
        if pass1 == pass2:
            if not username:
                messages.error(request, "Username is required.") 
            elif pass1 != pass2:
                messages.error(request, "Password Do Not Match!")
            elif User.objects.filter(username=username).exists():
                messages.error(request,"Username is Already Exist! ")
            else:
                user=User.objects.create_user(username)
                user.set_password(pass1)
                user.save()
                messages.success(request,"Your account has been created succecfully ")
        else:
            messages.error(request,"Password Not Match! ")
    return render(request,'Home/register.html')


@login_required
def Dashboard(request):
    return render(request,'Home/dashboard.html')

# How Import Works?
#  
def imports(request):
    if request.method == "POST":
        try:
            file_path = request.FILES.get('file_path')
            model_name = request.POST.get('model_name')
            if not file_path or not model_name:
                messages.error(request, 'Please provide both file and model name before submitting.')
                return redirect("/imports")

            with transaction.atomic():
                # Save uploaded file
                uploaded = upload.objects.create(file=file_path, model_name=model_name)
                absolute_path = uploaded.file.path

                # Validate CSV file against the model
                try:
                    check_csv_error(absolute_path, model_name)
                except CommandError as e:
                    messages.error(request,str(e))  # Display CommandError message in UI
                    return redirect("/imports")

                # Trigger asynchronous import task
                import_data_task.delay(absolute_path, model_name)
                messages.success(request, "Your data is being imported. You will be notified once it's done.")
                return redirect("/imports")

        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
            return redirect("/imports")
    # Display all available models
    allmodels = get_all_models()
    context = {'allmodels': allmodels}
    return render(request, "Home/import.html", context)


def export(request):
    if request.method == 'POST':
        model_name=request.POST.get('model_name')
        # try:
        #     call_command('exportByCSV',model_name)
        # except Exception as e:
        #     raise e
        try:
            export_data_task.delay(model_name)
            messages.success(request, "Your data is being Exported. You will be notified once it's done.")
        except Exception as e:
            raise e
    allmodels=get_all_models() 
    context={'allmodels':allmodels}
    return render(request,"Home/export.html",context)
 