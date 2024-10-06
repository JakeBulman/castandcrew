from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Event
from castandcrew.settings import MEDIA_ROOT, MEDIA_URL

# Create your views here.
@login_required
def dashboard(request):
	events=None
	if Event.objects.filter(event_organiser=request.user).exists():
		events = Event.objects.filter(event_organiser=request.user)
	return render(request, "events/dashboard.html",{'section':'dashboard','events':events,'media_root': MEDIA_ROOT, 'media_url': MEDIA_URL})

def event_details(request, id=None):
	event = Event.objects.get(id=id)
	return render(request, 'events/event_details.html',{'section':'dashboard','event':event})