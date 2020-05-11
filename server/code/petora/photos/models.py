from django.db import models
from django.utils import timezone
from users import models as user_models


class Photo(models.Model):
    profile = models.ForeignKey(user_models.Profile, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='photos')
    likes = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    user = models.ForeignKey(user_models.Profile, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE)
    likes = models.IntegerField()
    date_commented = models.DateTimeField(default=timezone.now)

