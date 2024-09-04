from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    website_link = models.TextField(blank=True, null=True)
    user_about = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    #portfolio pictures as a seperate model? (this allows for title and description)
    #portfolio audio as a seperate model? (this allows for title and description)
    #portfolio video as a seperate model? (this allows for title and description)
    
