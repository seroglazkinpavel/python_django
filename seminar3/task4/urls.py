from django.urls import path

from . import views


urlpatterns = [
    path('articles/<int:id_author>', views.AllArticlesViews.as_view(), name='articles'),
    path('article/<int:pk>', views.DetailArticle.as_view(), name='article'),
    path('add_author/', views.AddAuthor.as_view(), name='add_author'),
    path('author_page/<int:pk>', views.AuthorPage.as_view(), name='author_page'),
    path('add_article/', views.AddArticle.as_view(), name='add_article'),
]