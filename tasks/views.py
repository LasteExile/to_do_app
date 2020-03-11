import datetime

from django.shortcuts import render
from django.views.generic import ListView, TemplateView, FormView, DetailView
from django.db.models.functions import TruncDate
from django.http.response import HttpResponseRedirect

from . import models, forms


class Home(ListView):
    model = models.Task
    template_name = 'tasks/home.html'

    def post(self, request):
        params = request.POST.get('taskmarkas').split()
        type_ = int(params[0])
        key = int(params[1])

        if type_ == 1:
            models.Task.objects.filter(pk=key).update(completed=True)
        elif type_ == 2:
            models.Task.objects.filter(pk=key).update(completed=False)
        
        return HttpResponseRedirect('/tasks')
    
    def get_context_data(self, **kwards):
        context = super().get_context_data(**kwards)
        if self.request.user.is_authenticated:
            context['task_list'] = models.Task.objects.annotate(
                date=TruncDate('deadline_time')).order_by('-deadline_time').filter(user=self.request.user)
        return context


class Detail(DetailView):
    model = models.Task
    template_name = 'tasks/detail.html'

    def post(self, request, pk):
        params = request.POST.get('taskmarkas').split()
        type_ = int(params[0])
        key = int(params[1])

        if type_ == 1:
            models.Task.objects.filter(pk=key).update(completed=True)
        elif type_ == 2:
            models.Task.objects.filter(pk=key).update(completed=False)
        
        return HttpResponseRedirect(f'/tasks/detail/{pk}')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_tasks'] = models.Task.objects.get(pk=self.kwargs['pk']).sub_tasks.all()
        return context
    


class CreateTask(FormView):
    form_class = forms.CreateNewTaskForm
    template_name = 'tasks/create.html'
    success_url = '/tasks'

    def form_valid(self, form):
        time = form.cleaned_data.get('deadline_time')
        models.Task.objects.create(user=self.request.user, text=self.request.POST.get('text'), deadline_time=time)
        return HttpResponseRedirect(self.success_url)


class CreateSubTask(FormView):
    form_class = forms.CreateNewSubTaskForm
    template_name = 'tasks/createsub.html'
    success_url = '/tasks'

    def form_valid(self, form):
        models.SubTask.objects.create(task=self.request.POST.get('task'), text=self.request.POST.get('text'))
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

class About(TemplateView):
    template_name = 'tasks/about.html'
