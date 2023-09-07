from django.db import models
#from django.contrib.auth import get_user_model
from django.urls import reverse

#User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=225, verbose_name='Имя категории')
    slug = models.SlugField(max_length=225, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})


class Brand(models.Model):
    title = models.CharField(max_length=225, verbose_name='Название фирменного знака')
    slug = models.SlugField(max_length=225, verbose_name='Url', unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    MAYBECHOICE = [
        (0, 'No'),
        (1, 'Yes'),
    ]
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name='Фирменный знак', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=225, verbose_name='Наименование')
    slug = models.SlugField(max_length=225, verbose_name='Url', unique=True)
    #image = models.ImageField(verbose_name='Изображение')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    old_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Старая цена')
    status = models.PositiveSmallIntegerField(choices=MAYBECHOICE, blank=False, default=1, verbose_name='Статус')
    depart = models.CharField(max_length=225, verbose_name='Упаковка', blank=True)
    article = models.CharField(max_length=225, verbose_name='Артикуль', blank=True)
    grade = models.CharField(max_length=225, verbose_name='Класс', blank=True)
    height = models.CharField(max_length=100, verbose_name='Высота', blank=True)
    flower_size = models.CharField(max_length=225, verbose_name='Размер цветка', blank=True)
    flowering_period = models.CharField(max_length=100, verbose_name='Период', blank=True)
    landing_place = models.CharField(max_length=100, verbose_name='Место посадки', blank=True)
    frost_resistance = models.CharField(max_length=100, verbose_name='Морозостойкость', blank=True)
    # time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления', blank=True)

    def __str__(self):
        return self.title

    class Customer(models.Model):
        #user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
        name = models.CharField(max_length=225, verbose_name='Имя покупателя')
        phone = models.CharField(max_length=20, verbose_name='Номер телефона')
        address = models.CharField(max_length=225, verbose_name='Адрес')
        time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

        def __str__(self):
            return f'Имя покупателя: {self.name}'


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)  # поле для различения оплаченных и неоплаченных заказов

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity