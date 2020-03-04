from django.contrib import admin

from .models import Task, SubTask


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    pass

@admin.register(SubTask)
class SubTasksAdmin(admin.ModelAdmin):
    pass
