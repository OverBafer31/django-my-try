from django.db import models
from authentication.models import User
from kpi.models import KPI

class Goal(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(verbose_name='Название цели', max_length = 255)
    description = models.CharField(verbose_name='Описание', max_length = 255)
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    type = models.CharField(verbose_name='Тип', max_length = 255)
    kpi = models.ManyToManyField(KPI)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'




