from django.db import models
from exercise.models import Exercise

class Workout(models.Model):
    title = models.CharField(verbose_name='Тренировка', max_length = 255)
    description = models.TextField(verbose_name='Описание', default = False)
    type = models.IntegerField(verbose_name='Тип', default = False)
    calories = models.IntegerField(verbose_name='Калории', default = False)
    media = models.ImageField(verbose_name='Изображение', upload_to='workouts/images', default = False)
    gender = models.IntegerField(verbose_name='Пол', default = False)
    exercise = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'




