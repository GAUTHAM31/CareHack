# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from customer.models import donor
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect, HttpResponse

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import logout
import datetime
import random
import way2sms

def index(request):
	if request.user.is_authenticated():
		return redirect(home)
	else:
		return render(request,'index.html',{})


def logina(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['phno']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		try:
			p=donor.objects.get(user=user)
		except donor.DoesNotExist:
			p=None
		if user:
			if user.is_active and p.verify :
				login(request,user)
				return redirect(home)
				#return redirect(home)
			else:
				return HttpResponse("verify opt") #render(request,'otpfail.html',{}) 
		else:
			#HttpResponse("invaild")
			return HttpResponse("Try again")#render(request,'loginfail.html',{}) #redirect to invaild  username password url
	else:
		return redirect(index)#redirect if not post request was send



@login_required
def home(request):
	return HttpResponse("welcome")# render(request,'home.html',{})





def register(request):
	context = RequestContext(request)
	if request.method == 'POST':
		password 	= request.POST['password']
		fname 		= request.POST['fname']
		lname		= request.POST['lname']
		phno		= request.POST['phno']
		bg			= request.POST['bg']
		age			= request.POST['age']
		user = User.objects.create_user(username=phno,
                                 		password=password)
		user.save()
		rnum=random.randint(1000,9999)
		p=donor(user=user,
				  fname=fname,
				  lname=lname,
				  phno=phno,
				  blood_type=bg,
				  otp=rnum,
				  age=age,)
				  #otpdate=datetime.datetime.now())
		p.save()
		message="OTP"
		message+=str(rnum)
		pn=int(phno)
		q=way2sms.sms(8891821262,"way2sms3131")
		q.send(pn,message)
		n=q.msgSentToday()
		q.logout()
		return render(request,'otp.html',{'phno':phno})
		#
		#return render(request,'PatientPortal/otp.html',{})
	return redirect(logina)

def otpverify(request):
	context = RequestContext(request)

	if request.method == 'POST':
		phno= request.POST['phno']
		otp= request.POST['otp']
		try:
			p=donor.objects.get(phno=phno,otp=otp)
		except donor.DoesNotExist:
			p=None
		if p:
			p.verify=True
			return render(request,'otpsuc.html',{}) 
		else:
			return render(request,'otpfail.html',{}) 
	else:
		return redirect(logina)

# Create your views here.
