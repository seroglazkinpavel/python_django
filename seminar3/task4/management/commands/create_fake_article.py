import random
from django.core.management.base import BaseCommand
from task4.models import Article, Author


class Command(BaseCommand):
    help = "Generate fake article."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Article ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for a in Author.objects.all():
            for i in range(1, count + 1):
                article= Article(
                    title=f'Name{i}',
                    content=f'content {i} QWERTYUIOSDFGHJK',
                    publication_date='2000-01-01',
                    author=a,
                    category=f'Category{i}',
                    views=random.randint(1, 1000),
                    published=random.randint(0, 1)
                )
                article.save()
