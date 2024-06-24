from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "confirm_password"]

    def clean(self):
        cleaned_data = super().clean()
        confirm_password = cleaned_data.get("confirm_password")
        if confirm_password and self.cleaned_data.get('password') and confirm_password != self.cleaned_data.get('password'):
            self.add_error("confirm_password", _("Password doesn't match"))
    
    def save(self, commit: bool = True):
        user = super().save(commit=commit)
        user.last_login = timezone.now()
        if commit:
            user.save()
        return user
    

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("email", "password")