from django.urls import path

from flights.views import PlanetListView, FlightListView

urlpatterns = [
    path('/planet', PlanetListView.as_view()),
    path('/schedule', FlightListView.as_view())
]