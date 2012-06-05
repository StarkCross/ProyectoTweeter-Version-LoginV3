from django.db import models
from django.contrib.auth.models import User
#from thumbs import ImageWithThumbsField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name = 'lala')
    #nick_name = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50, blank = True, null = True)
    last_name = models.CharField(max_length = 50, blank = True, null = True)
    image_owner = models.ImageField (upload_to = 'photo',blank = True, null = True)
    #password = models.CharField(max_length = 50)
    birth_date = models.DateField(blank = True, null = True)
    #email = models.CharField(max_length = 50)
    place = models.CharField(max_length = 50, blank = True, null = True)
    biography = models.CharField(max_length = 50, blank = True, null = True)
    place_birth = models.CharField(max_length = 50, blank = True, null = True)
    follow = models.ManyToManyField('self', related_name='followers', blank = True, null = True)
   
    def __unicode__(self):
        return 'User: %s - %s %s' % (self.pk, self.last_name, self.first_name) 
   
def get_profile(user):
	if not hasattr(user, '_profile_cache'):
        	profile, created = Profile.objects.get_or_create(user=user)
        	user.profile_cache = profile
    	return user.profile_cache

User.get_profile = get_profile



class Tweet(models.Model):
    owner = models.ForeignKey('Profile', related_name='tweets')
    status = models.CharField(max_length = 50 )
    created_at = models.DateTimeField(auto_now_add=True)
