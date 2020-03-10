from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    deadline_time = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class SubTask(models.Model):
    task = models.ForeignKey('Task', related_name='sub_tasks', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
