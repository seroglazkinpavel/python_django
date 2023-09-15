from django.core.management.base import BaseCommand
from task5.models import Author


class Command(BaseCommand):
    help = "Generate fake author."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(
                first_name=f'Name{i}',
                last_name=f'Sername{i}',
                email=f'mail{i}@mail.ru',
                biography=f'biography {i} QWERTYUIOSDFGHJK',
                birthday='2000-01-01'
            )
            author.save()