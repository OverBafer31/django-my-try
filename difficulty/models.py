from django.db import models

class Difficulty(models.Model):
    title = models.CharField(verbose_name='Сложность', max_length = 255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сложность'
        verbose_name_plural = 'Сложности'
