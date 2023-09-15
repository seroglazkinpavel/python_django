from seminar2_task3 import views
from django.urls import path


urlpatterns = [
    path('author/', views.author, name='author'),

]