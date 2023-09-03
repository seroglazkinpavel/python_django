import random
from django.core.management.base import BaseCommand
from homework2.models import *


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        products = Product.objects.all()
        customer = Customer.objects.all()
        for i in range(1, count + 1):

            order = Order(
                customer=customer[random.randint(1, count)],
                product=products[random.randint(1, count)],
                total_amount=products[random.randint(1, count)].price,
                time_create='2023-01-01'
            )
            order.save()
            self.stdout.write(f'{order}')