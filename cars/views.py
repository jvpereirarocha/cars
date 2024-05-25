from django.views.generic import ListView

from cars.models import Vehicle


class VehicleListView(ListView):
    model = Vehicle
    template_name = "vehicles/list_of_vehicles.html"
    context_object_name = "vehicles"