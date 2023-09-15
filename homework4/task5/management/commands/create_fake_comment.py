import random
from django.core.management.base import BaseCommand
from task5.models import Article, User, Comment


class Command(BaseCommand):
    help = "Generate fake Comment."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Comment ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for u in User.objects.all():
            for p in Article.objects.all():
                for i in range(1, count + 1):
                    comment = Comment(
                        user=u,
                        article=p,
                        comment_text=f'content {i} QWERTYUIOSDFGHJK',
                        created_date='2000-01-01',
                        modified_date='2000-01-01',
                    )
                    comment.save()
