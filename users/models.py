from django.db import models
from django.contrib.auth.models import User
from trips.models import Trip


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(default='Moscow', max_length=30)
    saved_trips = models.ManyToManyField(Trip)

    def __str__(self):
        return f'{self.user.username} Profile'
