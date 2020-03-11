from django import forms
from datetime import datetime

class CreateNewTaskForm(forms.Form):
    text = forms.CharField(max_length=200)
    deadline_time = forms.DateTimeField(input_formats=[
        '%d/%m/%Y %H:%M', 
        '%d/%m/%Y',
        '%d.%m.%Y %H:%M', 
        '%d.%m.%Y',
        '%d-%m-%Y %H:%M', 
        '%d-%m-%Y',
        '%d %m %Y %H:%M', 
        '%d %m %Y',
        
        '%d/%m/%Y %H.%M', 
        '%d.%m.%Y %H.%M', 
        '%d-%m-%Y %H.%M', 
        '%d %m %Y %H.%M', 
        
        '%d / %m / %Y %H:%M', 
        '%d / %m / %Y',
        '%d . %m . %Y %H:%M', 
        '%d . %m . %Y',
        '%d - %m - %Y %H:%M', 
        '%d - %m - %Y',
        '%d %m %Y %H:%M', 
        '%d %m %Y',
        
        '%d / %m / %Y %H.%M', 
        '%d . %m . %Y %H.%M', 
        '%d - %m - %Y %H.%M', 
        ])

    def clean_deadline_time(self):
        time = self.cleaned_data['deadline_time']
        time_current = datetime.now()
        print(time)
        print(time_current)
        if time_current.replace(tzinfo=None) > time.replace(tzinfo=None):
            self.add_error('deadline_time', 'Please enter a valid future date')

        return time


class CreateNewSubTaskForm(forms.Form):
    text = forms.CharField(max_length=200)
    