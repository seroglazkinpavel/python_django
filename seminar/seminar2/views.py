from random import randint

from django.shortcuts import render
from django.http import HttpResponse
from seminar2.models import GameModel


def index(request):
    result = ('TAILS', 'HEADS')[randint(0, 1)]
    game = GameModel(result=result)
    game.save()
    return HttpResponse(f'{game}')


def last_game(request):
    last = GameModel().return_last(5)
    last_str = ['<br>' + str(i)for i in last]
    return HttpResponse(last_str)



