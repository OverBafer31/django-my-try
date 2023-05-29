from django.db import models

class Equipment(models.Model):
    title = models.CharField(verbose_name='Название оборудования', max_length = 255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'




