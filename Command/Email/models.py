from django.db import models
import uuid
# Create your models here.

class List(models.Model):
    email_list=models.CharField(max_length=50)
    def __str__(self):
        return self.email_list
    
    def count_emails(self):
        count=Subsciber.objects.filter(email_list=self).count()
        return count
    

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

class Sent(models.Model):
    email=models.ForeignKey(Email,related_name="sents",on_delete=models.CASCADE,null=True,blank=True)
    total_sent=models.IntegerField()

    def __str__(self):
        return f"{str(self.email)} - {str(self.total_sent)} Emails Sent"

class Email_Tracking(models.Model):
    email=models.ForeignKey(Email,on_delete=models.CASCADE)
    subscriber=models.ForeignKey(Subsciber,on_delete=models.CASCADE)
    unique_id=models.CharField(max_length=100,unique=True)
    open_at=models.DateTimeField(null=True,blank=True)
    click_at=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.email} - {self.subscriber}" 
