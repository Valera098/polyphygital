from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from datetime import datetime, timedelta

from gameblock.models import *

def shedule(request):
    current_time = datetime.now()
    start_date = current_time - timedelta(weeks=2)
    end_date = current_time + timedelta(weeks=2)
    games = Game.objects.all()
    finished_games = Game.objects.filter(is_finished=True, date_start__range=[start_date, current_time])
    unfinished_games = Game.objects.filter(is_finished=False, date_start__range=[current_time, end_date])
    context = {
        'title': 'Расписание',
        'games': games,
        'finished_games': finished_games,
        'unfinished_games': unfinished_games,
    }
    return render(request, 'gameblock/shedule.html', context=context)

def ratings(reqest):
    return HttpResponse('рейтинги игроков')
