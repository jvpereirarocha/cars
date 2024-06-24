from django.urls import path
from cars.views import RegisterView, VehicleListView, LoginView


app_name = 'cars'

urlpatterns = [
    path("register/", RegisterView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name='login'),
    path("vehicles/", VehicleListView.as_view(), name='vehicles_list'),
]