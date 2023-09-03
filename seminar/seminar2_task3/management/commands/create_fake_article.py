import random
from django.core.management.base import BaseCommand
from seminar2_task3.models import Author, Article, Category


class Command(BaseCommand):
    help = "Generate fake authors and article."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for c in Category.objects.all():
            for a in Author.objects.all():
                for j in range(1, count + 1):
                    article = Article(
                        title=f'Title{j}',
                        content=f'Text from {a.name} #{j} is bla bla bla many long text',
                        time_create=f'2000-01-{j}',
                        author=a,
                        category=c,
                        views=random.randint(1, 100),
                        publish=random.randint(0, 1)
                    )
                    article.save()
