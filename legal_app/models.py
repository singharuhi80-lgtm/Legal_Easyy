from django.db import models
from django.utils import timezone
# Create your models here.
##Contact Model##############

class Contact(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False)
    phone=models.CharField(max_length=13,null=False)
    query=models.TextField(default="",null=False)
    date=models.DateField(default=timezone.now,null=False)


    #########Feedback Model########

class Feedback(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False,primary_key=True)
    rating=models.CharField(max_length=5,null=False)
    remark=models.TextField(default="")
    date=models.DateField(default=timezone.now)

##########User#########

class User(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False,primary_key=True)
    password=models.CharField(max_length=50,null=False)
    phone=models.CharField(max_length=13,null=False)
    profile_pic=models.FileField(upload_to="user_pic/",default="")
    date=models.DateField(default=timezone.now,null=False)

########Legal Advisor#########
class LegalAdvisor(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False,primary_key=True)
    password=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=13,null=False)
    qualification=models.CharField(max_length=70)
    profile_pic=models.FileField(upload_to="advisor_pic/",default="")
    experience=models.CharField(max_length=80,null=False)
    skills=models.CharField(max_length=80,null=False)
    service_type=models.CharField(max_length=100,null=False)
   # date=models.DateField(default="timezone.now",null=False)


   #########service######
class LeagalService(models.Model):
    service_type=models.CharField(max_length=100,primary_key=True)
    service_description=models.TextField(default="",null=False)
    service_pic=models.FileField(upload_to="service_pic/",default="")
    

class ClientDocument(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    advisor_email=models.CharField(max_length=50)
    document_name=models.CharField(max_length=50,null=False)
    document_description=models.TextField()
    document_pic=models.FileField(upload_to="document_file/",default="")
    date=models.DateField(default=timezone.now)