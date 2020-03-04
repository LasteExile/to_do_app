from django.views.generic import FormView
from django.http import HttpResponseRedirect

from . import forms


class SignUpView(FormView):
    template_name = 'registration/signup.html'
    form_class = forms.SignUpForm
    success_url = '/home'

    def form_valid(self, form):
        form.create_new_user(self.request)
        return HttpResponseRedirect(self.success_url)

