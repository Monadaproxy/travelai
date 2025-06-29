from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)  # "Рим"
    dates = models.JSONField()  # {"start": "2025-05-15", "end": "2025-05-20"}
    itinerary = models.JSONField()  # {"День 1": [{"place": "Колизей", "time": "10:00"}]}
    bookings = models.JSONField(default=dict)  # {"Отель": {"link": "...", "price": 100}}