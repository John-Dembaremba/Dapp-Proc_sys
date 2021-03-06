from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=250)

    def __str__(self):
       return self.name

class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
   EthereumAccount = models.CharField(max_length=42, null=True)
   address = models.CharField(max_length=75, null=True)
   contacts = models.CharField(max_length=30, null=True)
   
   
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()