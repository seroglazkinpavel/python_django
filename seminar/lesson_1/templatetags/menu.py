from django import template
from lesson_1.models import Category

register = template.Library()


@register.inclusion_tag('lesson_1/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {"categories": categories, "menu_class": menu_class}
