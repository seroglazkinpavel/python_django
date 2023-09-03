from django.urls import path

from .views import *

urlpatterns = [
    path('type/', index, name='home'),

]