from django.db import models

# Create your models here.


class List(models.Model):
    email_list=models.CharField(max_length=50)

    def __str__(self):
        return self.email_list
    

class Subsciber(models.Model):
    email_list=models.ForeignKey(List,on_delete=models.CASCADE,null=True,blank=True)
    email_adress=models.EmailField(max_length=50)

    def __str__(self):
        return self.email_adress
    
class Email(models.Model):
    email_list=models.ForeignKey(List,on_delete=models.CASCADE,null=True,blank=True)
    subject=models.CharField(max_length=1000)
    body=models.TextField()
    attachment=models.FileField(upload_to="Email_Attachment/")
    sent_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    