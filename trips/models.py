from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)  # "Рим"
    start_date = models.DateField()
    end_date = models.DateField()
    itinerary = models.JSONField()  # {"День 1": [{"place": "Колизей", "time": "10:00"}]}
    bookings = models.JSONField(default=dict)  # {"Отель": {"link": "...", "price": 100}}
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Поездка'
        verbose_name_plural = 'Поездки'