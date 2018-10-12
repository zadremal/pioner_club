from django.db import models
from markdownx.models import MarkdownxField

import datetime


class Party(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    date = models.DateField(verbose_name='Дата')
    date_end = models.DateField(verbose_name="Дата окончания", blank=True, null=True)
    time_start = models.TimeField(default=datetime.time(22, 00), verbose_name='Начало мероприятия')
    time_end = models.TimeField(default=datetime.time(6, 00), blank=True, null=True,
                                verbose_name='Завершение мероприятия')
    description = MarkdownxField(verbose_name="Описание мероприятия")
    place = models.ForeignKey('Places', on_delete=models.CASCADE,  verbose_name='Место проведения')
    repeat = models.BooleanField(default=False,  verbose_name='Каджую неделю')
    active = models.BooleanField(default=True,  verbose_name='Активно')
    on_main = models.BooleanField(default=True,  verbose_name='Показывать на главной')
    poster = models.ImageField(upload_to="posters", verbose_name='Афиша')
    poster_alt = models.CharField(blank=True, max_length=255, verbose_name='Текст для афиши')

    def __str__(self):
        return '{} - {}'.format(self.date.strftime("%d.%m.%y"), self.name)

    class Meta:
        verbose_name_plural = 'Мероприятия'
        verbose_name = "Мероприятие"
        ordering = ['date']


class Places(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    location = models.CharField(max_length=255, default="пр-кт Испытателей 26/2", verbose_name="Адрес")
    open_hours = MarkdownxField(verbose_name="Режим работы")
    price = MarkdownxField(verbose_name="Цены")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Заведения'
        verbose_name = "Заведение"


class Deals(models.Model):
    name = models.CharField(verbose_name="Название акции", max_length=255)
    order = models.IntegerField(verbose_name="Порядок отображения", default=0)
    description = MarkdownxField(verbose_name="Описание акции")
    date_start = models.DateField(verbose_name="Дата начала акции", blank=True, null=True)
    date_end = models.DateField(verbose_name="Дата окончания акции", blank=True, null=True)
    on_main = models.BooleanField(verbose_name="На главной странице")
    poster = models.ImageField(upload_to="deals", verbose_name="Изображение")
    poster_alt = models.CharField(blank=True, max_length=255, verbose_name='Описание изображения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Акции"
        verbose_name = "Акция"
        ordering = ["order"]


class Units(models.Model):
    unit = models.CharField(max_length=32, verbose_name='Сокращение')
    description = models.CharField(max_length=64,  verbose_name='Полное наименование')

    def __str__(self):
        return self.unit

    class Meta:
        verbose_name_plural = "Меню - Единицы измерения"
        verbose_name = "Единица измерения"


class MenuCategories(models.Model):
    name = models.CharField(verbose_name="Категории меню", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Меню - Места реализации"
        verbose_name = "Меню - Место реализации"


class Countries(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=1, verbose_name="Порядок")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order"]



class DishCategories(models.Model):

    menu_category = models.ForeignKey('MenuCategories', related_name='sub_category',
                                      on_delete=models.CASCADE, verbose_name="Категория меню")
    order = models.IntegerField(blank=True, null=True, verbose_name="Порядок отображения")
    dish_category = models.CharField(max_length=255, verbose_name="Категория блюда")
    dish_category_description = models.CharField(max_length=255, blank=True, verbose_name="Описание категории блюд")

    def __str__(self):
        return '{} - {}'.format(self.menu_category, self.dish_category)

    class Meta:
        verbose_name_plural = "Меню - Категории блюд"
        verbose_name = "Меню - Категория блюда"


class Dish(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    category = models.ForeignKey("DishCategories", related_name="dish", on_delete=models.CASCADE,
                                 verbose_name="Категория")
    details = models.TextField(verbose_name="Дополнительно", blank=True, null=True)
    net = models.FloatField(verbose_name="Вес/объем")
    units = models.ForeignKey('Units', on_delete=models.CASCADE, verbose_name="Единица измерения")
    price = models.IntegerField(verbose_name="Стоимость")
    iiko_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}. {}".format(self.category, self.name)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Меню"
        verbose_name = "Позиция"
        ordering = ["category"]


class BottleBeer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    details = models.TextField(verbose_name="Дополнительно", blank=True, null=True)
    alcohol = models.FloatField(verbose_name="Алкоголь")
    country = models.ForeignKey("Countries", related_name="bottle_beer", verbose_name="Страна",
                                on_delete=models.CASCADE)
    net = models.FloatField(verbose_name="Объем")
    price = models.IntegerField(verbose_name="Стоимость")
    iiko_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}. {}".format(self.country, self.name)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Пиво Бутылочное"
        verbose_name = "Пиво"
        ordering = ["country"]


class Beer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    details = models.TextField(verbose_name="Дополнительно", blank=True, null=True)
    alcohol = models.FloatField(verbose_name="Алкоголь")
    country = models.ForeignKey("Countries", related_name="beer", verbose_name="Страна",
                                on_delete=models.CASCADE)
    price03 = models.IntegerField(verbose_name="Стоимость за 0,3")
    price05 = models.IntegerField(verbose_name="Стоимость за 0,5")
    iiko_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}. {}".format(self.country, self.name)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Пиво Разливное"
        verbose_name = "Пиво"
        ordering = ["name"]


class Leads(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")
    reserve_date = models.DateField(blank=True, null=True, verbose_name="Дата брони")
    name = models.CharField(max_length=256, verbose_name="Имя")
    phone = models.CharField(max_length=12, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")

    def __str__(self):
        return "{} - {}".format(self.date.strftime("%d.%m.%y"), self.phone)

    class Meta:
        verbose_name_plural = "Заявки - бронирования"
        verbose_name = "Заявка"


class Birthdays(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")
    birthday_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата ДР")
    name = models.CharField(max_length=256, verbose_name="Имя")
    phone = models.CharField(max_length=12, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")

    def __str__(self):
        return "{} - {}".format(self.date.strftime("%d.%m.%y"), self.phone)

    class Meta:
        verbose_name_plural = "Заявки - дни рождения"
        verbose_name = "Заявка"


class Bankets(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")
    banket_date = models.DateField(blank=True, null=True, verbose_name="Дата банкета")
    name = models.CharField(max_length=256, verbose_name="Имя")
    phone = models.CharField(max_length=12, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return "{} - {}".format(self.date.strftime("%d.%m"), self.phone)

    class Meta:
        verbose_name_plural = "Заявки - банкеты"
        verbose_name = "Заявка"


class Feedbacks(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")
    name = models.CharField(max_length=256, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    text = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return "Сообщение с контактной формы"

    class Meta:
        verbose_name_plural = "Заявки - обратная связь"
        verbose_name = "Заявка"


class Newyears(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")
    reserve_date = models.DateField(blank=True, null=True, verbose_name="Дата брони")
    name = models.CharField(max_length=256, verbose_name="Имя")
    phone = models.CharField(max_length=12, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")

    def __str__(self):
        return "{} - {}".format(self.date.strftime("%d.%m.%y"), self.phone)

    class Meta:
        verbose_name_plural = "Заявки на новый год"
        verbose_name = "Заявка"


class Newyear_Corporates(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")
    reserve_date = models.DateField(blank=True, null=True, verbose_name="Дата брони")
    name = models.CharField(max_length=256, verbose_name="Имя")
    phone = models.CharField(max_length=12, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")

    def __str__(self):
        return "{} - {}".format(self.date.strftime("%d.%m.%y"), self.phone)

    class Meta:
        verbose_name_plural = "Новгодние корпоративы"
        verbose_name = "Корпоратив"