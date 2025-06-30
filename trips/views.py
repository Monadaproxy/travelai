from django.http import JsonResponse
from django.shortcuts import render
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
                itinerary = generate_itinerary(destination, dates, interests)
                print(itinerary)
                itinerary = json.loads(itinerary)
                print(itinerary)
                return render(request, 'trips/save.html', {'itinerary': itinerary})

            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'trips/plan.html', {'form': form})

@require_POST
def save_trip(request):
    try:
        data = request.POST
        trip = Trip.objects.create(
            user=request.user,
            destination=data.get('destination'),
            start_date=data.get('start_date'),
            end_date=data.get('end_date'),
            interests=data.get('interests'),
            itinerary=json.loads(data.get('itinerary'))
        )
        print('СОХРАНИЛ')
        return JsonResponse({'status': 'success', 'trip_id': trip.id})
    except Exception as e:
        print(f'НЕ СОХРА7НИЛ {e}')
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

