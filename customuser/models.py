from django.contrib.auth.models import AbstractUser
from django.db import models
from technology.models import Technology,Subtechnology,Topic
from datetime import datetime

class CustomUser(AbstractUser):
    phone = models.TextField(blank=True, null=True, 
    max_length=10,)
    is_codeexpert  = models.BooleanField(default=False)
    is_instructor  = models.BooleanField(default=False)
    is_freelancer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    otp = models.CharField(blank=True, max_length=255,null=True)
    summary = models.TextField(max_length=500, blank=True)
    security_question = models.CharField(max_length=30, blank=True)
    security_answer = models.CharField(max_length=30, blank=True)
    pincode = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    technology = models.ManyToManyField(Technology, blank=True, null=True)
    sub_technology = models.ManyToManyField(Subtechnology, blank=True, null=True)
    topic = models.ManyToManyField(Topic, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    last_seen =  models.DateTimeField(default=datetime.now(),null=True, blank=True)
    profile_pic =  models.ImageField(upload_to ='profile_pics/',null=True,blank=True, max_length=255)
    verification_code = models.CharField(max_length=30, blank=True)
    total_experience = models.FloatField(null=True, blank=True, default=None)
    relevant_experience = models.FloatField(null=True, blank=True, default=None)
    date_of_birth =  models.DateField(default=datetime.now(),null=True, blank=True)

    def __str__(self):
        return self.username