from django.core.management.base import BaseCommand
from seminar2_task3.models import Author


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(
                name=f'Name{i}',
                surname=f'Sername{i}',
                email=f'mail{i}@mail.ru',
                bio='QWERTYUIOSDFGHJK',
                bd='2000-01-01'
            )
            author.save()

