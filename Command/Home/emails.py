from django.core.mail import send_mail
from django.conf import settings

def send_email(email_recipients, subject, message):
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  # From email address
        email_recipients,    # List of recipients
        fail_silently=False, # Raise errors on failure
    )