from django.apps import apps
from django.core.management import CommandError
import csv
from datetime import datetime
import os
from django.conf import settings
# Function to get all models except default ones
def get_all_models():
    """
    Fetches all custom model names except default ones provided by Django.
    Default models include those used for authentication, content types, sessions, etc.

    Returns:
        list: A list of custom model names (strings).
    """
    default_models = ["LogEntry", "Permission", "Group", "User", "ContentType", "Session", "upload"]
    custom_models = []

    # Iterate through all models in the project
    for model in apps.get_models():
        # Exclude default models
        if model.__name__ not in default_models:
            custom_models.append(model.__name__)
    
    return custom_models


# Function to check CSV file for errors based on the model structure
def check_csv_error(file_path, model):
    """
    Validates the structure of a CSV file against a specified Django model.

    Args:
        file_path (str): The path to the CSV file to validate.
        model (str): The name of the model to validate the CSV file against.

    Raises:
        CommandError: If the model is not found or if the CSV file's structure
                      does not match the model fields.

    Returns:
        models.Model: The matched Django model.
    """
    models = None

    # Iterate through all app configurations to find the specified model
    for app_config in apps.get_app_configs():
        try:
            # Attempt to fetch the model from the current app's config
            models = apps.get_model(app_config.label, model)
            break  # Exit loop if the model is found
        except LookupError:
            # Ignore if the model is not found in the current app config
            continue

    # If the model is not found in any app, raise an error
    if not models:
        raise CommandError(f"Model {model} not found in any app")
    
    # Extract field names from the model, excluding the 'id' field
    model_field = [field.name for field in models._meta.fields if field.name != 'id']
    # print(F"Model_field- {model_field}")
    try:
        # Open the CSV file for reading
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            # Extract the headers from the CSV file, stripping any extra spaces
            csv_header = [header.strip() for header in reader.fieldnames]
            # print(csv_header) 

            # Compare CSV headers with model fields
            if csv_header != model_field:
                raise CommandError(
                    f"CSV file does not match with model fields ({model})."
                )
    except CommandError as e:
        # Re-raise CommandError for further handling
        raise e
    
    # Return the matched model if validation is successful
    return models





def generate_csv_file(models):
    current = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    export_dirs=os.path.join(settings.MEDIA_ROOT,"Export")
    file_path=os.path.join(export_dirs,f"Export-{models.__name__}-Data_{current}.csv")
    return file_path