from django.db import models
from authentication.models import User
from exercise.models import Exercise

class Schedule(models.Model):
    user = models.ManyToManyField(User)
    workout = models.ManyToManyField(Exercise)
    date = models.DateField(verbose_name='Дата', default = False)
    time = models.TimeField(verbose_name='Время', default = False)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
