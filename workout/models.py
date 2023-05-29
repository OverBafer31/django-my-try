from django.db import models
from exercise.models import Exercise
from type.models import Type
from equipment.models import Equipment

class Workout(models.Model):
    title = models.CharField(verbose_name='Тренировка', max_length = 255)
    description = models.CharField(verbose_name='Описание', default = False, max_length = 255)
    image = models.ImageField(verbose_name='Обложка', upload_to='workouts/images', default = False)
    type = models.ManyToManyField(Type)
    difficulty = models.CharField(verbose_name='Сложность', default = False, max_length = 255)
    time = models.IntegerField(verbose_name='Длительность', default = False)
    calories = models.IntegerField(verbose_name='Калории', default = False)
    gender = models.CharField(verbose_name='Пол', default = False, max_length = 255)
    inventory = models.ManyToManyField(Equipment)
    exercise = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'




