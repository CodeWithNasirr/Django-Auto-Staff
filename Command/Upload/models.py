from django.db import models

# Create your models here.

class upload(models.Model):
    file=models.FileField(upload_to="Import/")
    model_name=models.CharField(max_length=50)
    upload_at=models.DateTimeField(auto_now_add=True)