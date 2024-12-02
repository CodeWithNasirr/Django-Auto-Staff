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
    message = """
Dear User,

We are pleased to inform you that your data has been successfully imported into our system.

Summary of the Import:
- Import Status: Completed Successfully

Should you have any questions or encounter any issues, please do not hesitate to reach out to our support team.

Thank you for choosing our services.

Best regards,  
[xyzx]  
[Support Contact Information]
"""

    email = "sknasiruddin665@gmail.com"#yaha per user ka email hoga jo user lgoin keya hoga khudka email dekar
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
    email = "facts3989@gmail.com"
    send_email([email],subject,message,attachment=file_path)
    return 'Data Exported Succesfully'
        