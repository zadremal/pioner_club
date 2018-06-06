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
    price = MarkdownxField(verbose_name="Цены")


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

class Units(models.Model):
    unit = models.CharField(max_length=32)
    description = models.CharField(max_length=64)

    def __str__(self):
        return self.unit

    class Meta:
        verbose_name_plural = "Единицы измерения"


class MenuCategories(models.Model):
    name = models.CharField(verbose_name="Категории меню", max_length=255)

    def __str__(self):
        return self.name

class DishCategories(models.Model):
    menu_category = models.ForeignKey('MenuCategories', related_name='sub_category', on_delete=models.CASCADE)
    dish_category = models.CharField(max_length=255)
    dish_category_description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.menu_category, self.dish_category)


class Dish(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey("DishCategories", related_name="dish", on_delete=models.CASCADE)
    consist = models.TextField()
    net = models.FloatField()
    units = models.ForeignKey('Units', on_delete=models.CASCADE)
    price = models.IntegerField()
    iiko_id = models.IntegerField(blank=True, null= True)

    class Meta:
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Leads(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    reserve_date = models.DateField(blank=True, null = True)
    name = models.CharField(max_length=256, verbose_name="Имя")
    phone = models.CharField(max_length=12, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.date.strftime("%d.%m.%y"), self.phone)

    class Meta:
        verbose_name_plural = "Заявки - бронирования"


class Birthdays(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    birthday_date = models.DateTimeField(blank=True, null = True)
    name = models.CharField(max_length=256, verbose_name="Имя")
    phone = models.CharField(max_length=12, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.date.strftime("%d.%m.%y"), self.phone)

    class Meta:
        verbose_name_plural = "Заявки - дни рождения"


class Bankets(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    banket_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=256, verbose_name="Имя")
    phone = models.CharField(max_length=12, verbose_name="Телефон")
    email = models.EmailField()

    def __str__(self):
        return "{} - {}".format(self.date.strftime("%d.%m"), self.phone)

    class Meta:
        verbose_name_plural = "Заявки - банкеты"
