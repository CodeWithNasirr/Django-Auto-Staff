from django.shortcuts import render,redirect
from Email.models import List,Email,Subsciber
from django.contrib import messages
from Email.task import send_email_task
def send_emails(request):
    if request.method=="POST":
        Email_list=request.POST.get('Email-List')
        subject=request.POST.get('subject')
        body=request.POST.get('body')
        file_path = request.FILES.get('Attachment')
        list_instance, created = List.objects.get_or_create(email_list=Email_list)
        email=Email(email_list=list_instance,subject=subject,body=body,attachment=file_path)
        email.save()
        attachment=email.attachment.path
        subscriber=Subsciber.objects.filter(email_list=list_instance)
        email_addres=[email.email_adress for email in subscriber]
        send_email_task.delay(email_addres,subject,body,attachment)
        messages.success(request, "Your Email Sent Successfully..")
        return redirect("/Email/send-email")
        
    allmodels=List.objects.all()
    context={'allmodels':allmodels}
    return render(request,"Email/send-email.html",context)