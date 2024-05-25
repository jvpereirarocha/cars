from django.urls import path
from cars.views import VehicleListView


urlpatterns = [
    path("vehicles/", VehicleListView.as_view())
]