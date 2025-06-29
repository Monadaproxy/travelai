from django.http import JsonResponse
from django.shortcuts import render
from .forms import TripPlanForm
from .planner import generate_itinerary



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
                return render(request, 'trips/plan.html', {'itinerary': itinerary})

            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'trips/plan.html', {'form': form})
