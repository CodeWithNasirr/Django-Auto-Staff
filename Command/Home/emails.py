from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from Email.models import Email,Sent,Email_Tracking,Subsciber
import uuid
from django.conf import settings
from bs4 import BeautifulSoup


def send_email(email_recipients, subject, message,attachment=None,email_id=None):
    new_message = message
    for recipient_email in email_recipients:
        #Create Email Tracking Record
        if email_id:
            email=Email.objects.get(pk=email_id)
            subscriber=Subsciber.objects.get(email_list=email.email_list,email_adress=recipient_email)
            unique_id=str(uuid.uuid4()).split("-")[0]
            email_tracking = Email_Tracking.objects.create(
                email=email,
                subscriber=subscriber,
                unique_id=unique_id
            )
            #Generate the tracking pixel
            click_tracking_url=f"{settings.BASE_URL}email/track/click/{unique_id}"
            open_tracking_url=f"{settings.BASE_URL}email/track/open/{unique_id}"

            # print(f"click_tracking_url---> {click_tracking_url}")
            # print(f"open_tracking_url---> {open_tracking_url}")

            #Search for the links in the email body
            soup=BeautifulSoup(message,'html.parser')
            urls=[a['href'] for a in soup.find_all('a',href=True)]

            #if there are links or url in the email body we will injedxt our tacking url to that links
            if urls:
                for url in urls:
                    #make the final Tracling Url
                    tracking_url=f"{click_tracking_url}?url={url}"
                    new_message=new_message.replace(f"{url}",f"{tracking_url}")
            else:
                print("No Url Found In The Email Content ")
            
            open_tracking_img = f"<img src='{open_tracking_url}' width='1' height='1' style='display:none;' >"

            if not message.strip():
                new_message = f"<p>This is a system-generated email.</p>{open_tracking_img}"
            else:
                new_message += open_tracking_img

        print(f'new_message-->{new_message}')
        mail=EmailMessage(subject=subject,body=new_message,from_email=settings.DEFAULT_FROM_EMAIL,to=email_recipients)
        mail.content_subtype = "html"
        if attachment is not None:
            mail.attach_file(attachment)
        mail.send(fail_silently=False)

    # Store the total sent emails inside the Sent Model
    if email:
        sent=Sent()
        sent.email=email
        sent.total_sent=email.email_list.count_emails()
        sent.save()
        