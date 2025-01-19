from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Image_Compression(models.Model):
    Quality_Choices=[(i,i) for i in range(10,101,10)]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    orginal_image=models.ImageField(upload_to="original_images/")
    Quality=models.IntegerField(choices=Quality_Choices,default=80) 
    Compress_image=models.ImageField(upload_to="Compress_images/")
    compress_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"
    