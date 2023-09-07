from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Author, Article


class AllArticlesViews(TemplateView):
    template_name = 'task4/articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.get(pk=self.kwargs['id_author'])
        articles = Article.objects.filter(author=author).all()
        context['articles'] = articles
        return context


class DetailArticle(DetailView):
    model = Article
    template_name = 'task4/detail_article.html'
    context_object_name = 'article' # переопределили название obj

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj