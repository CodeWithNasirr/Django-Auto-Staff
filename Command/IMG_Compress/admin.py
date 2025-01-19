from django.contrib import admin
from .models import Image_Compression
from django.utils.html import format_html

# Register your models here.

class Image_list(admin.ModelAdmin):
    def thumbnail(self,obj):
        return format_html(f"<img src='{obj.Compress_image.url}' width='50' height='50'> ")

    def ori_image_size(self,obj):
        return format_html(f"{obj.orginal_image.size/(1024*1024):.2f}MB")
    
    def compr_image_size(self,obj):
        size_in_mb=obj.Compress_image.size/(1024*1024)
        if size_in_mb>1:
            return format_html(f"{size_in_mb:.2f}MB")
        else:
            size_in_kb=obj.Compress_image.size/1024
            return format_html(f"{size_in_kb:.2f}KB")
    
    list_display=("user","thumbnail","ori_image_size","compr_image_size","compress_at")
    

admin.site.register(Image_Compression,Image_list)
