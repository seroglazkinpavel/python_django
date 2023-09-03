import random
from django.core.management.base import BaseCommand
from homework2.models import Product


class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(
                title=f'Title{i}',
                description=f'Text #{i} is bla bla bla many long text',
                price=random.randint(100, 1000),
                quantity=random.randint(1, 10),
                time_create='2023-01-01'
            )
            product.save()
            self.stdout.write(f'{product}')