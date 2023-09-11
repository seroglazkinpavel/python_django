from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView
from .models import Author, Article
from task4 import forms


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


class AddAuthor(CreateView):
    model = Author
    template_name = 'task4/add_author.html'
    form_class = forms.AddAuthorForm
    # success_url = reverse_lazy('author_page')


class AuthorPage(DetailView):
    model = Author
    template_name = 'task4/author_page.html'


class AddArticle(CreateView):
    model = Article
    template_name = 'task4/add_article.html'
    form_class = forms.AddArticleForm
