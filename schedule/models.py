from django.db import models
from authentication.models import User
from workout.models import Workout

class Schedule(models.Model):
    user = models.ManyToManyField(User)
    workout = models.ManyToManyField(Workout)
    date = models.DateField(verbose_name='Дата', default = False)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
