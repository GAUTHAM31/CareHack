# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import donor

# Register your models here.
class donorAdmin(admin.ModelAdmin):
	list_display = ['user','did','fname','lname','phno','verify','otp','blood_type','credits']

admin.site.register(donor,donorAdmin)


