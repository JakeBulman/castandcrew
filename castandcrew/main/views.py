from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Profile
from castandcrew.settings import MEDIA_ROOT, MEDIA_URL

# Create your views here.
def landing_page(request):
	profile = Profile.objects.get(user_id=request.user)
	my_profile = None
	if request.user.is_authenticated:
		my_profile = Profile.objects.get(user_id=request.user)
	return render(request, "main/landing_page.html",{'section':'landing_page','profile':profile,'media_root': MEDIA_ROOT, 'media_url': MEDIA_URL, 'my_profile':my_profile})

