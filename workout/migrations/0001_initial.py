# Generated by Django 4.2.1 on 2023-05-17 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тренировка')),
                ('description', models.TextField(default=False, verbose_name='Описание')),
                ('type', models.IntegerField(default=False, verbose_name='Тип')),
                ('calories', models.IntegerField(default=False, verbose_name='Калории')),
                ('media', models.ImageField(default=False, upload_to='workouts/images', verbose_name='Изображение')),
                ('gender', models.IntegerField(default=False, verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Тренировка',
                'verbose_name_plural': 'Тренировки',
            },
        ),
    ]