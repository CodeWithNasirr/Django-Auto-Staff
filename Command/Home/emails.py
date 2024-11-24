from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings

def send_email(email_recipients, subject, message,attachment=None):
    email=EmailMessage(subject=subject,body=message,from_email=settings.DEFAULT_FROM_EMAIL,to=email_recipients)
    if attachment is not None:
        email.attach_file(attachment)
    email.send(fail_silently=False)
