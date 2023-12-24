from django.db.models.signals import  post_save
#The signal get fired everytime a model is saved
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


#We want a user profile created everytime a user is created
#when post_save signal is send by the User when it is created the function will be invoked
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
