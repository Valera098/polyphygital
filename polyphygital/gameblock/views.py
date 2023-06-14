from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render

from gameblock.models import *
def shedule(request):
    games = Game.objects.all()
    context = {
        'title' : 'Расписание',
        'games': games,
    }

    return render(request, 'gameblock/shedule.html', context=context)

def ratings(reqest):
    return HttpResponse('рейтинги игроков')
