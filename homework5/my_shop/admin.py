from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}

@admin.action(description='Сбросить количество в ноль')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['title', 'category', 'quantity', 'get_photo']
    ordering = ['category', 'quantity']
    list_filter = ['time_create', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    """Отдельный продукт."""
    #fields = ['title', 'description', 'category', 'time_create', 'rating']
    readonly_fields = ['time_create', 'rating']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields':['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'time_create'],
            }
        ),
    ]

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50>")
        return '_'


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Order)

