from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile, Discipline
from django.contrib import messages
from castandcrew.settings import MEDIA_ROOT, MEDIA_URL

@login_required
def dashboard(request):
	profile = Profile.objects.get(user_id=request.user)
	return render(request, "account/dashboard.html",{'section':'dashboard','profile':profile,'media_root': MEDIA_ROOT, 'media_url': MEDIA_URL})

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			#create user obj but don't save until after password validation
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			#Create user profile attached to this account
			Profile.objects.create(user=new_user)
			return render(request,'account/register_done.html',{'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request,'account/register.html',{'user_form':user_form})


@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user,data=request.POST,prefix="user")
		profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES,prefix="profile")
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Profile updated successfully')
		else:
			messages.error(request, 'Error updating your profile')
	else:
		user_form = UserEditForm(instance=request.user,prefix="user")
		profile_form = ProfileEditForm(instance=request.user.profile,prefix="profile")
	return render(request,'account/edit.html',{'user_form':user_form,'profile_form':profile_form})

def profile_search(request):
	profiles = Profile.objects.all()
	return render(request, 'account/profile_search.html',{'section':'dashboard','profiles':profiles})

def profile_details(request, id=None):
	profile = Profile.objects.get(id=id)
	return render(request, 'account/profile_details.html',{'section':'dashboard','profile':profile})

def discipline_list(request):
	disciplines = Discipline.objects.filter(parent_discipline__isnull=True)
	return render(request, 'account/discipline_list.html',{'section':'discipline_list','disciplines':disciplines})