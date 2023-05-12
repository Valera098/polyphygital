from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Ты находишься на <b>ГЛАВНОЙ</b> странице');

def news(request):
    return HttpResponse('Ты находишься на <b>НОВОСТНОЙ</b> странице');

def pageNotFound(request, exception):
    return HttpResponse('Ты находишься на <b>СТРАНИЦЕ ОШИБКИ</b>');
    # return render(request, 'newsblock/404.html', {'menu': menu, 'title': 'Упс...'})
