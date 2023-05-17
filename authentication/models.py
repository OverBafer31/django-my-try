from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from authentication.managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    firstname = models.CharField(verbose_name="Имя",max_length=255)
    avatar=models.ImageField(verbose_name="Аватар", upload_to='user_image', default=False, blank=True)
    gender=models.CharField(verbose_name="Пол",max_length=255, null = True, blank=True)
    height=models.CharField(verbose_name="Рост",max_length=255, null = True, blank=True)
    weight=models.CharField(verbose_name="Вес",max_length=255, null = True, blank=True)
    age=models.CharField(verbose_name="Возраст",max_length=255, null = True, blank=True)
    preparation=models.FloatField(verbose_name="Подготовка",default=1.0, null = True, blank=True)
    email=models.EmailField(verbose_name="Email",max_length=255,unique=True)

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

