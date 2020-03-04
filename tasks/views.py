from django.shortcuts import render
from django.views.generic import ListView

from . import models


class Home(ListView):
    model = models.Task
    template_name = 'tasks/home.html'

