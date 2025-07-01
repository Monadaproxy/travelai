from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import TripPlanForm
from .planner import generate_itinerary
from .models import Trip
import json




def generate_trip(request):
    form = TripPlanForm()
    if request.method == 'POST':
        form = TripPlanForm(request.POST)
        if form.is_valid():
            destination = form.cleaned_data['destination']
            dates = f"{form.cleaned_data['start_date']} - {form.cleaned_data['end_date']}"
            interests = form.cleaned_data['interests']

            try:
                itinerary = json.loads(generate_itinerary(destination, dates, interests))
                trip = Trip.objects.create(
                    user=request.user,
                    destination=destination,
                    start_date=form.cleaned_data['start_date'],
                    end_date=form.cleaned_data['end_date'],
                    itinerary=itinerary,
                    hotel=itinerary['hotel']
                )
                return redirect('trips:list')

            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'trips/plan.html', {'form': form})

def trips_list(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, 'trips/list.html', {'trips': trips})

@require_POST
def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, user=request.user)
    trip.delete()
    return redirect('trips:list')




