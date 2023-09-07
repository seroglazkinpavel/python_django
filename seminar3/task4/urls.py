from django.urls import path

from . import views


urlpatterns = [
    path('articles/<int:id_author>', views.AllArticlesViews.as_view(), name='articles'),
    path('article/<int:pk>', views.DetailArticle.as_view(), name='article'),
]