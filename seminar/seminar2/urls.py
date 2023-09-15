from seminar2 import views
from django.urls import path


urlpatterns = [
    path('index/', views.index, name='index'),
    path('last/', views.last_game, name='last_game'),
]