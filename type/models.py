from django.db import models

class Type(models.Model):
    title = models.CharField(verbose_name='Тип', max_length = 255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'




