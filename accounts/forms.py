from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    def create_new_user(self, request):
        User.objects.create_user(username=request.POST.get(
            'username'), email=request.POST.get('email'), password=request.POST.get('password1'))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
