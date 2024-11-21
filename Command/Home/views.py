from django.contrib import messages
from django.shortcuts import render,redirect
from .utils import get_all_models
from django.core.management import call_command,CommandError
from django.db import transaction
from django.core.mail import send_mail
from Upload.models import upload
from Home.task import import_data_task
from Home.utils import check_csv_error


def index(request):
    if request.method == "POST":
        try:
            file_path = request.FILES.get('file_path')
            model_name = request.POST.get('model_name')

            if not file_path or not model_name:
                messages.error(request, 'Please provide both file and model name before submitting.')
                return redirect("/")

            with transaction.atomic():
                # Save uploaded file
                uploaded = upload.objects.create(file=file_path, model_name=model_name)
                absolute_path = uploaded.file.path

                # Validate CSV file against the model
                try:
                    check_csv_error(absolute_path, model_name)
                except CommandError as e:
                    messages.error(request,str(e))  # Display CommandError message in UI
                    return redirect("/")

                # Trigger asynchronous import task
                import_data_task.delay(absolute_path, model_name)
                messages.success(request, "Your data is being imported. You will be notified once it's done.")
                return redirect("/")

        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
            return redirect("/")

    # Display all available models
    allmodels = get_all_models()
    context = {'allmodels': allmodels}
    return render(request, "Home/index.html", context)