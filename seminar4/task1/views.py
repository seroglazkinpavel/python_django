import logging
from django.shortcuts import render
from .forms import GameForm
from random import randint
from .utils import HeadsOrTails, Dice, RandomNumbers


logger = logging.getLogger(__name__)


def game_view(request):
    results = []
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['game']
            game = globals()[game_type]()
            attempt = form.cleaned_data['attempt']
            for i in range(attempt):
                game.play()
                results.append(str(game))
    else:
        form = GameForm()
    return render(request, 'task1/game_form.html', {'results': results, 'form': form, 'title': 'игра'})

def game_form(request):
    results = []
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            attempt = form.cleaned_data['attempt']
            if game == 'М':
                result = [('TAILS', 'HEADS')[randint(0, 1)] for i in range(attempt)]
            elif game == 'K':
                result = [[randint(1, 6)] for i in range(attempt)]
            else:
                result = [[randint(1, 100)] for i in range(attempt)]
            results.append(result)
            logger.info(f'Получили {game=}, {attempt=}.')
    else:
        form = GameForm()
    context = {'title': 'Игра', 'results': results, 'form': form}
    return render(request, 'task1/game_form.html', context=context)

