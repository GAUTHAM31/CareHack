# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import uuid
import datetime 

class donor(models.Model):
	def __unicode__(self):
		return unicode(self.user)
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	did=models.UUIDField(default=uuid.uuid4, editable=False)
	fname=models.CharField(max_length=20)
	lname=models.CharField(max_length=20)
	age=models.IntegerField(default=30)
	longitude = models.DecimalField(max_digits=8, decimal_places=3,null=True)
	lat = models.DecimalField(max_digits=8, decimal_places=3,null=True)
	credits=models.IntegerField(default=0)
	ld=models.DateField(null=True)
	phno=models.IntegerField(max_length=10)
	blood_list=(('1','A+'),('2','A-'),('3','B+'),('4','B-'),('5','AB+'),('6','AB-'),('7','O+'),('8','O-'))
	blood_type=models.CharField(max_length=5,choices=blood_list,default='1')
	otp=models.IntegerField(default=0)
	otpdate=models.DateTimeField(null=True)
	verify=models.BooleanField(default=False)
	times=models.IntegerField(default=0,null=True)
	#img= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
	
class companies(models.Model):
	cid=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
	credits=models.IntegerField(default=0)

class coupon(models.Model):
	credid=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
	credits=models.IntegerField(default=0)
	companies=models.ForeignKey(companies, on_delete=models.CASCADE)
	details=models.CharField(max_length=180)	
	used=models.BooleanField(default=False)
	companycredid=models.CharField(max_length=200,default="----")
	donor=models.ForeignKey(donor, on_delete=models.CASCADE, null=True)
class requests(models.Model):
	rid=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)	
	blood_list=(('1','A+'),('2','A-'),('3','B+'),('4','B-'),('5','AB+'),('6','AB-'),('7','O+'),('8','O-'))
	blood_type=models.CharField(max_length=5,choices=blood_list,default='1')
	location=models.CharField(max_length=20)
	
# Create your models here.
