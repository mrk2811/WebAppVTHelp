from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from vt_help.models import placesOfInterest
# Create your models here.



class Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(default="regular", max_length=50)
    campus = models.CharField(max_length=100)

@receiver(post_save, sender=User)
def create_user_details(sender, instance, created, **kwargs):
    if created:
        Details.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_details(sender, instance, **kwargs):
    instance.details.save()


class Comments(models.Model):
    text = models.TextField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(placesOfInterest, on_delete=models.CASCADE)


