from django.db import models
from django.conf import settings
from django.urls import reverse

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "users/{0}/{1}".format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    website_link = models.TextField(blank=True, null=True)
    user_about = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True)
    #portfolio pictures as a seperate model? (this allows for title and description)
    #portfolio audio as a seperate model? (this allows for title and description)
    #portfolio video as a seperate model? (this allows for title and description)

    class Meta:
        ordering = ['stage_name']
        indexes = [models.Index(fields=['stage_name'])]

    def __str__(self):
        return self.stage_name
    
    def get_absolute_url(self):
        return reverse('profile_details',args=[self.id])

