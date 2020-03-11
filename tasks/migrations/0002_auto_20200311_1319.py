# Generated by Django 2.2 on 2020-03-11 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtask',
            name='additional_text',
        ),
        migrations.RemoveField(
            model_name='task',
            name='additional_text',
        ),
        migrations.RemoveField(
            model_name='task',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='task',
            name='reapeted',
        ),
        migrations.AddField(
            model_name='subtask',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_tasks', to='tasks.Task'),
        ),
    ]
