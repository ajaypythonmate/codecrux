# from django.db import models
# from customuser.models import CustomUser
# import uuid
# # Create your models here.
#
#
# class Beneficiary(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
#                              related_name='beneficiary_user', null=True, blank=True)
#     beneId = models.CharField(max_length=20)
#     name = models.CharField(max_length=100, blank=True, null=True)
#     email = models.CharField(max_length=200, blank=True, null=True)
#     phone = models.CharField(max_length=12, blank=True, null=True)
#     bankAccount = models.CharField(max_length=18, blank=True, null=True)
#     ifsc = models.CharField(max_length=11, blank=True, null=True)
#     address = models.CharField(max_length=150, blank=True, null=True)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     pincode = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.name+str(self.id)
#
#
# class Transactions(models.Model):
#     transferId = models.CharField(max_length=20)
#     orderId = models.CharField(max_length=150)
#     status = models.CharField(max_length=50)
#     amount = models.CharField(max_length=50)
#     revenue = models.CharField(max_length=50)
#     date = models.DateTimeField('date', auto_now=True)
#
#     def __str__(self):
#         return self.orderId
