from django.db import models

class Exercise(models.Model):
    title = models.CharField(verbose_name='Упражнение', max_length = 255)
    media = models.ImageField(verbose_name='Медиа', upload_to='exercises/images', default = False)
    type = models.CharField(verbose_name='Тип', max_length = 255)
    time = models.IntegerField(verbose_name='Длительность', default = False)
    amount = models.IntegerField(verbose_name='Кол-во повторений', default = False)
    calories = models.IntegerField(verbose_name='Калории', default = False)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'




