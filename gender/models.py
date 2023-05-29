from django.db import models

class Gender(models.Model):
    title = models.CharField(verbose_name='Пол', max_length = 255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'
