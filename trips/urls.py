from django.urls import path
from . import views

app_name = 'trips'

urlpatterns = [
    path('plan/', views.generate_trip, name='plan'),
    path('list/', views.trips_list, name='list'),
]