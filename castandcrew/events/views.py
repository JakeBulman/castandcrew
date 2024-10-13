from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Event
from account.models import Profile
from castandcrew.settings import MEDIA_ROOT, MEDIA_URL

# Create your views here.
@login_required
def dashboard(request):
	events=None
	if Event.objects.filter(event_organiser=request.user).exists():
		events = Event.objects.filter(event_organiser=request.user)
	my_profile = None
	if request.user.is_authenticated:
		my_profile = Profile.objects.get(user_id=request.user)
	return render(request, "events/dashboard.html",{'section':'dashboard','events':events,'media_root': MEDIA_ROOT, 'media_url': MEDIA_URL, 'my_profile':my_profile})

def event_details(request, id=None):
	event = Event.objects.get(id=id)
	my_profile = None
	if request.user.is_authenticated:
		my_profile = Profile.objects.get(user_id=request.user)
	return render(request, 'events/event_details.html',{'section':'dashboard','event':event, 'my_profile':my_profile})

# def new_event(request):
# 	if request.method == 'POST':
# 		user_form = UserRegistrationForm(request.POST)
# 		if user_form.is_valid():
# 			#create user obj but don't save until after password validation
# 			new_user = user_form.save(commit=False)
# 			new_user.set_password(user_form.cleaned_data['password'])
# 			new_user.save()
# 			#Create user profile attached to this account
# 			Profile.objects.create(user=new_user)
# 			return render(request,'account/register_done.html',{'new_user': new_user})
# 	else:
# 		user_form = UserRegistrationForm()
# 	return render(request,'account/register.html',{'user_form':user_form})