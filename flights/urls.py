from django.urls import path

from flights.views import PlanetListView

urlpatterns = [
    path('/planet', PlanetListView.as_view())
]