import random
from django.core.management.base import BaseCommand
from homework2.models import Customer


class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            customer = Customer(
                name=f'Title{i}',
                phone=89278656712,
                address=f'Address{i}',
                time_create='2023-01-01'
            )
            customer.save()
            self.stdout.write(f'{customer}')