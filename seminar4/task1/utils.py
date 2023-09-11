import random


class Game:
    def __init__(self):
        self.result = None

    def play(self):
        pass

    def __self__(self):
        return str(self.result)


class HeadsOrTails(Game):
    def play(self):
        self.result = random.choice(['Heads', 'Tails'])


class Dice(Game):
    def play(self):
        self.result = random.randint(1, 6)


class RandomNumbers(Game):
    def play(self):
        self.result = random.randint(1, 100)