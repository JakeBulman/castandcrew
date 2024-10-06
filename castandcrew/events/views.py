from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Profile
from castandcrew.settings import MEDIA_ROOT, MEDIA_URL

# Create your views here.
@login_required
def dashboard(request):
	profile = Profile.objects.get(user_id=request.user)
	return render(request, "account/dashboard.html",{'section':'dashboard','profile':profile,'media_root': MEDIA_ROOT, 'media_url': MEDIA_URL})
