from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта')
    biography = models.TextField(max_length=1000, verbose_name='Биография')
    birthday = models.DateField(verbose_name='День рождения')

    def get_absolute_url(self):
        return reverse('author_page', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    title = models.CharField(max_length=225, verbose_name='Имя категории', unique=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    article = models.ForeignKey('Article', verbose_name='Статья', on_delete=models.CASCADE)
    comment_text = models.TextField(verbose_name='Текст комментария')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.user.first_name}'

    class Meta:
        ordering = ['-id']


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название статьи')
    content = models.TextField(max_length=1000, verbose_name='Текст')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор статьи')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    published = models.BooleanField(default=False, verbose_name='Опубликована или нет')

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Title is: {self.title}'


