from django import forms
from task4 import models


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ['first_name', 'last_name', 'email', 'biography', 'birthday']


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'content', 'author', 'category']
