from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField(max_length=1000)
    birthday = models.DateField()

    def get_absolute_url(self):
        return reverse('author_page', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        #return f'Comment by {self.author.first_name} {self.author.last_name} on {self.article}'
        return f'{self.user.first_name}'

    class Meta:
        ordering = ['-id']


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Title is: {self.title}'

