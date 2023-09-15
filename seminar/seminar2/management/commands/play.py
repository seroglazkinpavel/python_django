from random import randint
from django.core.management import BaseCommand

from seminar2.models import GameModel


class Command(BaseCommand):
    help = 'Play game Head and Tails'

    def handle(self, *args, **kwargs):
        result = ('TAILS', 'HEAD')[randint(0, 1)]
        game = GameModel(result=result)
        game.save()
        self.stdout.write(f'{game}')  # нужно приводить к строке
