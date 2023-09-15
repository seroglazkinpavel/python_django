from django.db import models
from decimal import Decimal


class Product(models.Model):
    title = models.CharField(max_length=225, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')

    def __str__(self):
        return f'{self.title}, {self.price}'

    @staticmethod
    def get_cost(n):
        return Product.price * n


class Customer(models.Model):
    name = models.CharField(max_length=225, verbose_name='Имя покупателя')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=225, verbose_name='Адрес')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return f'Имя покупателя: {self.name}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая сумма')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время оформления')

    def __str__(self):
        return '{}'.format(self.id)
