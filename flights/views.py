import json, datetime

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from flights.models import FlightSchedule, Planet

class PlanetListView(View):
    def get(self, request):
        
        planets = Planet.objects.all()

        result = [
            {
                'planet_id' : planet.id,
                'planet_name' : planet.name,
                'planet_code' : planet.code
            } for planet in planets]

        return JsonResponse({'planet_list' : result}, status = 200)

class FlightListView(View):
    def get(self, request):

        departure_planet_id = request.GET.get('departure_planet_id', None)
        arrival_planet_id = request.GET.get('arrival_planet_id', None)
        departure_datetime = request.GET.get('departure_datetime', None)
        arrival_datetime = request.GET.get('arrival_datetime', None)
        seat_type = request.GET.get('seat_type', None)

        q = Q()

        if departure_planet_id:
            q &= Q(departure_planet_id = departure_planet_id)
        
        if arrival_planet_id:
            q &= Q(arrival_planet_id = arrival_planet_id)

        if departure_datetime:
            q &= Q(departure_datetime = departure_datetime)

        if arrival_datetime:
            q &= Q(arrival_datetime = arrival_datetime)

        if seat_type:
            q &= Q(seat_type = seat_type)

        flight_filter = FlightSchedule.objects.select_related(
            'seat_type',
            'departure_planet_id',
            'arrival_planet_id',
            'departure_datetime',
            'arrival_datetime'
        ).filter(q)