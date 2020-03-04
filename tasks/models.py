from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    additional_text = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now=True)
    deadline_time = models.DateTimeField()
    reapeted = models.CharField(max_length=1, choices=(
        ('y', 'Yearly'),
        ('m', 'Monthly'),
        ('w', 'Weekly'),
        ('d', 'Dayly'),
        ('n', 'No repeat'),
    ), default='n')

    def __str__(self):
        return self.text


class SubTask(models.Model):
    task = models.ForeignKey('Task', related_name='sub_tasks', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    additional_text = models.TextField(blank=True)

    def __str__(self):
        return self.text
