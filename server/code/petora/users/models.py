from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    profile_picture = models.ImageField(upload_to='profile_photos', default='profile_photos/default_profile_pic.jpg')
    created_at = models.DateField(default=timezone.now)
    is_private = models.BooleanField(default=False)
    is_enabled = models.BooleanField(default=True)
    followed_by = models.IntegerField(default=0)
    follows = models.IntegerField(default=0)
    type = models.CharField(max_length=30, default=None, null=True)
    breed = models.CharField(max_length=40, default=None, null=True)

    def __str__(self):
        return self.name + ' profile'


class Follows(models.Model):
    followed_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followed_profile')
    followed_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followedby')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


