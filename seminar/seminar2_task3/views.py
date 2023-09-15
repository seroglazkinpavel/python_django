#from django.shortcuts import render
from django.http import HttpResponse
from seminar2_task3.models import Author


def author(request):
    res = Author.objects.all()
    res_str = ['<br>'+str(i)for i in res]
    return HttpResponse(res_str)
