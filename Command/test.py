import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Command.settings'
django.setup()
# Create your tests here.

from django.apps import apps
def app_config(model):
    model_instance = None
    for app_config in apps.get_app_configs():
        try:
            model_instance = apps.get_model(app_config.label, model)
            break
        except LookupError:
            continue
    if not model_instance:
        print('Model Not Exists')
    else:
        print(f'Model {model} found in app {app_config.label}')
# app_config('Student')

