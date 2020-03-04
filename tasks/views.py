from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from . import models


class Home(ListView):
    model = models.Task
    template_name = 'tasks/home.html'

class About(TemplateView):
    template_name='tasks/about.html'

