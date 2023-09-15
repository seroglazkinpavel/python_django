from django.core.management.base import BaseCommand
from homework2.models import Product


class Command(BaseCommand):
    help = "Get all products."

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for i in products:
            self.stdout.write(f'{i}')
