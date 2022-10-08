from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


class Register(CreateView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "registration/register.html"
