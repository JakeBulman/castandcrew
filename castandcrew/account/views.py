from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def test_view(request):
	context = {}
	return render(request, "main/base.html", context=context)

def user_login(request):
	if request.mmethod == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			clean_form = form.cleaned_data
			user = authenticate(request,
					   username=clean_form['username'],
					   password=clean_form['password'])
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponse('Autheticated Successfully')
				else:
					return HttpResponse('Disabled Account')
			else:
				return(HttpResponse('Invalid Login'))
	else:
		form = LoginForm()
	return render(request, 'account/login.html', {'form':form})