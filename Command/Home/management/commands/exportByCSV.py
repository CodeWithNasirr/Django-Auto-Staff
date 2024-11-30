from django.core.management import BaseCommand,CommandError
from datetime import datetime
from django.apps import apps
import csv
from Home.utils import generate_csv_file
class Command(BaseCommand): 
    def add_arguments(self, parser):
        parser.add_argument('model-name',type=str,help='Get Model Name')

    def handle(self, *args, **options):
        model_name=options['model-name'].capitalize()
        # print(f"Model_name: {model_name} ")

        models=None
        for model_config in apps.get_app_configs():
            try:
                models=apps.get_model(model_config.label,model_name)
                break
            except LookupError:
                continue
        if not models:
            raise CommandError(f"Model {models.__name__} not found in any app")

        
        model=models.objects.all()
        file_path=generate_csv_file(models)

        with open(file_path,'w',newline="")as file:
            writer=csv.writer(file)
            writer.writerow([field.name for field in models._meta.fields])

            for dt in model:
                writer.writerow([getattr(dt,field.name)for field in models._meta.fields])#getattr(obj,attr)
            
        self.stdout.write(self.style.SUCCESS("Data Exported Sucessfully..."))