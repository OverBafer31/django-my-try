# Generated by Django 4.2.1 on 2023-05-29 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_alter_schedule_time_alter_schedule_workout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='time',
        ),
    ]
