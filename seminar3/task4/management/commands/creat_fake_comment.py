import random
from django.core.management.base import BaseCommand
from task4.models import Article, Author, Comment


class Command(BaseCommand):
    help = "Generate fake Comment."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Comment ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for a in Author.objects.all():
            for p in Article.objects.all():
                for i in range(1, count + 1):
                    comment = Comment(
                        author=a,
                        article=p,
                        comment_text=f'content {i} QWERTYUIOSDFGHJK',
                        created_date='2000-01-01',
                        modified_date='2000-01-01',
                    )
                    comment.save()