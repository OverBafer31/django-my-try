from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from authentication.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(verbose_name="Имя", max_length = 255)
    avatar = models.ImageField(verbose_name="Фото пользователя", upload_to='users/avatars', default = False)
    gender = models.BooleanField(verbose_name='Пол', default = False)
    height = models.IntegerField(verbose_name='Рост', default = False)
    weight = models.IntegerField(verbose_name='Вес', default = False)
    age = models.IntegerField(verbose_name='Возраст', default = False)
    preparation = models.FloatField(verbose_name='Уровень подготовки', default = False)
    email = models.EmailField(verbose_name="Email", max_length = 255, unique  = True)
    # password_salt = models.CharField(verbose_name="Пароль", max_length = 255)
    # password_hash = models.CharField(verbose_name="Пароль", max_length = 255)

    is_active =models.BooleanField(verbose_name='Активирован',default=False)
    is_staff=models.BooleanField(verbose_name='Персонал',default=False)
    is_superuser=models.BooleanField(verbose_name='Администратор',default=False)
    is_client = models.BooleanField(verbose_name='Клиент', default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['firstname']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'




