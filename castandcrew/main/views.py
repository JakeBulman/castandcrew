from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Profile
from castandcrew.settings import MEDIA_ROOT, MEDIA_URL

# Create your views here.
def landing_page(request):
    my_profile = None
    if request.user.is_authenticated:
        my_profile = Profile.objects.get(user_id=request.user)
    if request.user.id == None:
        #this is the "public" user
        my_profile = Profile.objects.get(user_id=9)
          		
    return render(request, "main/landing_page.html",{'section':'landing_page','media_root': MEDIA_ROOT, 'media_url': MEDIA_URL, 'my_profile':my_profile})

