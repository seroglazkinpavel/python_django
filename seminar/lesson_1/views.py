from django.shortcuts import render
import logging
from django.http import HttpResponse

from lesson_1.models import Brand, Category, Product

logger = logging.getLogger(__name__)

menu = [
    {'title': "О нас", 'url_name': 'about'},
    {'title': "Новости", 'url_name': 'news'},
    {'title': "Условия работы", 'url_name': 'working_conditions'},
    {'title': "Отзывы", 'url_name': 'reviews'},
    {'title': "Контакты", 'url_name': 'contacts'},
    {'title': "Статьи", 'url_name': 'articles'}
]


def index(request):
    logger.info('Index page accessed')
    brands = Brand.objects.all()
    products = Product.objects.order_by("-id")[0:8]
    context = {
        'title': 'Главная страница',
        'menu': menu,
        'brands': brands,
        'products': products
    }
    return render(request, 'lesson_1/index.html', context=context)


def get_category(request):
    return render(request, 'lesson_1/category.html')


def about(request):
    logger.info('About page accessed')
    return render(request, 'lesson_1/about.html', {'menu': menu, 'title': 'О нас'})


def news(request):
    logger.info('News page accessed')
    return HttpResponse('Новости')


def working_conditions(request):
    logger.info('Working_conditions page accessed')
    return HttpResponse('Условия работы')


def reviews(request):
    logger.info('Reviews page accessed')
    return HttpResponse('Отзывы')


def contacts(request):
    logger.info('Contacts page accessed')
    return HttpResponse('Контакты')


def articles(request):
    logger.info('Articles page accessed')
    return HttpResponse('Статьи')
