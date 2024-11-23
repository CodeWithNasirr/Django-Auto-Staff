from celery import shared_task
from django.core.management import call_command
from Home.emails import send_email
@shared_task
def import_data_task(absolute_path, model_name):
    try:
        call_command("importByCSV",absolute_path, model_name)
    except Exception as e:
        raise e
    # Notify the user by email
    subject='TestMail'
    message="Your Data Imported Sucessfully"
    email = "sknasiruddin665@gmail.com"
    send_email([email],subject,message) 
    return 'Data Imported Succesfully'
        