from django.urls import path
from . import views

app_name = 'trips'

urlpatterns = [
    path('plan/', views.generate_trip, name='plan'),
    path('save/', views.save_trip, name='save_trip'),
]