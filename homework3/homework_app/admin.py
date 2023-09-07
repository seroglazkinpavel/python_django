from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'time_create', 'modified_date')
    list_display_links = ('id', 'title')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'total_amount', 'time_create', 'modified_date')
    #list_display_links = ('id', 'name')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'address', 'time_create', 'modified_date')
    list_display_links = ('id', 'name')


admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
