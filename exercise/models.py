from django.db import models

class Exercise(models.Model):
    title = models.CharField(verbose_name='Упражнение', max_length = 255)
    hardness = models.FloatField(verbose_name='Сложность', default = False)
    amount = models.IntegerField(verbose_name='Кол-во повторений', default = False)
    media = models.ImageField(verbose_name='Изображение', upload_to='exercises/images', default = False)
    show_timer = models.BooleanField(verbose_name='Таймер', default = False)
    calories = models.IntegerField(verbose_name='Калории', default = False)
    equipment = models.IntegerField(verbose_name='Экипировка', default = False)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'




