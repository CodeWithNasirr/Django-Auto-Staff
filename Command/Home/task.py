from celery import shared_task
from django.core.management import call_command
from Home.emails import send_email
from datetime import datetime
from Home.utils import generate_csv_file
from django.apps import apps
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
        

@shared_task       
def export_data_task(model_name):
    try:
        call_command("exportByCSV",model_name)
    except Exception as e:
        raise e
    
    models=None
    for model_config in apps.get_app_configs():
        try:
            models=apps.get_model(model_config.label,model_name)
            break
        except LookupError:
            continue
    file_path=generate_csv_file(models)
    # Notify the user by email
    subject='Export Data' 
    current = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    message=f"Your Data Exported Sucessfully at time {current} "
    email = "sknasiruddin665@gmail.com"
    send_email([email],subject,message,attachment=file_path)
    return 'Data Exported Succesfully'
        