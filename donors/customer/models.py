# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class donor(models.Model):
	def __unicode__(self):
		return unicode(self.user)
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	did=models.IntegerField()
	fname=models.CharField(max_length=20)
	lname=models.CharField(max_length=20)
	age=models.IntegerField()
	longitude = models.DecimalField(max_digits=8, decimal_places=3)
	lat = models.DecimalField(max_digits=8, decimal_places=3)
	credits=models.IntegerField()
	ld=models.DateField()
	bt=models.CharField(max_length=10)
	phno=models.IntegerField(max_length=10)
	
class companies(models.Model):
	cid=models.IntegerField()
	credits=models.IntegerField()

class coupon(models.Model):
	credid=models.IntegerField()
	credits=models.IntegerField()
	cid=models.IntegerField()
	details=models.CharField(max_length=180)
	did=models.IntegerField()

# Create your models here.
