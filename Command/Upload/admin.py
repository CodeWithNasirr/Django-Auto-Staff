from django.contrib import admin
from .models import upload
# Register your models here.
class UploadAdmin(admin.ModelAdmin):
    list_display=['model_name','upload_at']
admin.site.register(upload,UploadAdmin)