from django.db import models

class KPI(models.Model):
    title = models.CharField(verbose_name='Название KPI', max_length = 255)
    calories = models.IntegerField(verbose_name='Калории', default = False)
    type = models.CharField(verbose_name='Тип', max_length = 255)
    amount = models.IntegerField(verbose_name='Кол-во повторений', default = False)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'KPI'
        verbose_name_plural = 'KPIs'
