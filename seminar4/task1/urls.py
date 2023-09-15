from django.urls import path
from . import views

urlpatterns = [
    path('game/', views.game_form, name='game'),
    path('game_view/', views.game_view, name='game_view'),
]