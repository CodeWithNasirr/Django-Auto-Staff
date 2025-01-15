from django.shortcuts import render,redirect,get_object_or_404,HttpResponse,HttpResponseRedirect
from Email.models import List,Email,Subsciber,Sent,Email_Tracking
from django.contrib import messages
from Email.task import send_email_task
from django.db.models import Sum
from django.utils import timezone 
def send_emails(request): 
    if request.method=="POST": 
        Email_list=request.POST.get('Email-List')
        subject=request.POST.get('subject')
        body=request.POST.get('body')
        file_path = request.FILES.get('Attachment')
        
        list_instance, created = List.objects.get_or_create(email_list=Email_list)
        email=Email(email_list=list_instance,subject=subject,body=body)
        if file_path:
            email.attachment=file_path
        email.save()

        subscriber=Subsciber.objects.filter(email_list=list_instance)
        email_addres=[email.email_adress for email in subscriber]

        if email.attachment: 
            attachment=email.attachment.path
        else:
            attachment=None

        email_id = email.id

        send_email_task.delay(email_addres,subject,body,attachment,email_id)
        messages.success(request, "Your Email Sent Successfully..")
        return redirect("/email/send-email")
        
    allmodels=List.objects.all()
    context={'allmodels':allmodels}
    return render(request,"Email/send-email.html",context)



def tracking_dash(request):
    emails=Email.objects.all().annotate(total_sent=Sum("sents__total_sent"))

    context={"emails":emails,}
    return render(request,"Email/tracking_dash.html",context)


def email_statics(request,pk):
    email=get_object_or_404(Email,pk=pk)
    sents = email.sents.all()
    # sents=Sent.objects.filter(email=email)
    context={
        "email":email,
        "sents": sents,
    }
    return render(request,"Email/email-statics.html",context)


def track_click(request,unique_id):
    try:
        email_tracking=Email_Tracking.objects.get(unique_id=unique_id)
        url=request.GET.get('url')
        print(url)
        
        if not email_tracking.click_at:
            email_tracking.click_at=timezone.now()
            email_tracking.save()
            return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect(url)
            
    except:
        return HttpResponseRedirect(url)


def track_open(request,unique_id):
    try:
        email_tracking = Email_Tracking.objects.get(unique_id=unique_id)
        if not email_tracking.open_at:
            email_tracking.open_at=timezone.now()
            email_tracking.save()
            return HttpResponse("Email  openend Succesfully..")
        else:
            return HttpResponse("Email already opend")
    except:
        return HttpResponse("Email already opend ")

