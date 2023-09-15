from django.views.generic import TemplateView, DetailView, CreateView
from .models import Author, Article, Comment
from task5.forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect


class AllArticlesViews(TemplateView):
    template_name = 'task5/articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.get(pk=self.kwargs['id_author'])
        articles = Article.objects.filter(author=author).all()
        context['articles'] = articles
        return context


class DetailArticle(DetailView):
    model = Article
    template_name = 'task5/detail_article.html'
    context_object_name = 'article'
    form_class = CommentForm

    # def get_queryset(self):
    #     return Comment.objects.filter(article=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=self.kwargs['pk'])
        context['title'] = 'Cтраница статья'
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj


# class AddAuthor(CreateView):
#     model = Author
#     template_name = 'task5/add_author.html'
#     form_class = forms.AddAuthorForm


class AuthorPage(DetailView):
    model = Author
    template_name = 'task5/author_page.html'


# class AddArticle(CreateView):
#     model = Article
#     template_name = 'task4/add_article.html'
#     form_class = forms.AddArticleForm

def article_single(request, pk):
    article = get_object_or_404(Article, id=pk)
    comments = Comment.objects.filter(article=pk).order_by("-id")[0:5]
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.article = article
            form.save()
            return redirect(article_single, pk)
    else:
        form = CommentForm()
    return render(request, 'task5/article_single.html',
                  {'article': article,
                   'comments': comments,
                   'form': form
                   }
    )

