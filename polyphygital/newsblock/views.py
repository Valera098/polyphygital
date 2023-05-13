from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from newsblock.models import *


def index(request):
    return render(request, 'newsblock/index.html', {'title': 'Главная'});

def news(request):
    posts = News.objects.all()

    context = {
        'posts': posts,
        'title': 'Новости',
    }

    return render(request, 'newsblock/news.html', context=context);

def show_post(request, post_id):
    post = get_object_or_404(News, id=post_id)

    context = {
        'title':post.title,
        'post': post,
    }

    return render(request, 'newsblock/post.html', context=context);

def pageNotFound(request, exception):
    return HttpResponse('Ты находишься на <b>СТРАНИЦЕ ОШИБКИ</b>');
    # return render(request, 'newsblock/404.html', {'menu': menu, 'title': 'Упс...'})
