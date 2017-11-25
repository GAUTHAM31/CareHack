# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from customer.models import donor
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect, HttpResponse

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import logout

def index(request):
	if request.user.is_authenticated():
		return redirect(home)
	else:
		return render(request,'',{})


def logina(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		try:
			empl=employee.objects.get(user=user)
		except employee.DoesNotExist:
			empl=None
		if empl:
			login(request,user)
		else:
			#HttpResponse("invaild")
			return redirect(tryagain)#redirect to invaild  username password url
	else:
		return redirect(index)#redirect if not post request was send
def tryagain(request):
	return render(request,'',{})
# Create your views here.
