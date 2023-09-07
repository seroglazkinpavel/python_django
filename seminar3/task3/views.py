from django.shortcuts import render

from django.http import HttpResponse
from random import randint
from django.views.generic import TemplateView


def heads_tails(request):
    return HttpResponse('HEADS' if randint(0, 1) else 'TAILS')#('TAILS', 'HEADS')[randint(0, 1)]


class GameView(TemplateView):
    template_name = 'task3/game.html'


class HeadGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        result = [('TAILS', 'HEADS')[randint(0, 1)] for i in range(self.kwargs['count'])]
        context['result'] = result
        context['title'] = 'Игра в орла и решку'
        return context


def cube(request, number_of_throws):
    list_cube = []
    for i in range(number_of_throws):
        list_cube.append(str(randint(1, 6)))
    context = {
        'title': 'Cube',
        'list_cube': list_cube
    }
    return render(request, 'task3/cube.html', context=context)


def random_num(request):
    return HttpResponse(str(randint(1, 100)))
