# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import donor

# Register your models here.
class donorAdmin(admin.ModelAdmin):
	list_display = ['user','did','fname','lname','phno','verify','otp','blood_type','credits']

admin.site.register(donor,donorAdmin)


>>>>>>> d156a1b3ebd650889ea8873e90e0f15060933ccd
