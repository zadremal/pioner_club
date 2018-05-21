from django.db import models

# Create your models here.
from django.db import models
from markdownx.models import MarkdownxField

import datetime


# Create your models here.

class Party(models.Model):
    name = models.CharField(max_length=255, verbose_name= 'Название вечерники')
    date = models.DateField()
    time_start = models.TimeField(default=datetime.time(22,00))
    time_end = models.TimeField(default=datetime.time(6,00), blank=True, null=True)
    description = MarkdownxField(verbose_name="Описание мероприятия")
    place= models.ForeignKey('Places', on_delete=models.CASCADE)
    repeat = models.BooleanField(default=False)
    active = models.BooleanField(default = True)
    on_main = models.BooleanField(default = True)
    poster = models.ImageField(upload_to="posters", verbose_name="Изображение")
    poster_alt = models.CharField(blank=True, max_length=255, verbose_name='Описание изображения')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Вечерники'


class Places(models.Model):
    name = models.CharField(max_length=255, verbose_name="Место проведения мероприятия")
    location = models.CharField(max_length=255, default="пр-кт Испытателей 26/2", verbose_name="Адрес")
    open_hours = MarkdownxField(verbose_name="Режим работы")
    price = MarkdownxField(verbose_name="Цены на вход")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Заведения'

class Deals(models.Model):
    name = models.CharField(verbose_name="Название акции", max_length=255)
    description = MarkdownxField(verbose_name="Описание акции")
    date_start = models.DateField(verbose_name="Дата начала акции", blank=True, null=True)
    date_end = models.DateField(verbose_name="Дата окончания акции", blank=True, null=True)
    on_main = models.BooleanField(verbose_name="На главной странице")
    poster = models.ImageField(upload_to="deals", verbose_name="Изображение")
    poster_alt = models.CharField(blank=True, max_length=255, verbose_name='Описание изображения' )

    def __str__(self):

        return self.name

    class Meta:
        verbose_name_plural = "Акции"
        verbose_name = "Акция"
