from django.urls import path

from .views import *


urlpatterns = [
    #path('cube/<int:number_of_throws>', cube, name='cube'),
    path('head/<int:count>', HeadGame.as_view(), name='head'),
]
