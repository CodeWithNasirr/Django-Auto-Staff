from celery import shared_task
from Home.emails import send_email

@shared_task
def send_email_task(email_addres,subject,body,attachment):
    send_email(email_addres,subject,body,attachment)
    return "Email Sending Task Excecuted Succesfully.."