from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
	return render(request, "account/dashboard.html",{'section':'dashboard'})



