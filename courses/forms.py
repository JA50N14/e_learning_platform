from django.forms.models import inlineformset_factory
from .models import Course, Module
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

ModuleFormSet = inlineformset_factory(
    Course,
    Module,
    fields= ['title', 'description'],
    extra=2,
    can_delete=True
)


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
