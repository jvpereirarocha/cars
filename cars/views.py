from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.models import User

from cars.forms import LoginForm, RegisterForm
from cars.models import Vehicle


class LoginView(View):
    form_class = LoginForm
    template_name = "auth/login.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return redirect('cars:vehicles_list')
        
        return render(request, self.template_name, {"form": form})


class RegisterView(View):
    form_class = RegisterForm
    template_name = "auth/register.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('cars:login')
        
        return render(request, self.template_name, {"form": form})


class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = "vehicles/list_of_vehicles.html"
    context_object_name = "vehicles"