from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('working_conditions/', working_conditions, name='working_conditions'),
    path('reviews/', reviews, name='reviews'),
    path('contacts/', contacts, name='contacts'),
    path('articles/', articles, name='articles'),
]