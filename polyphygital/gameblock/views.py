from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from datetime import datetime, timedelta
from django.db.models import Q
from rest_framework import viewsets

from gameblock.models import *
from gameblock.serializers import *


def shedule(request):
    current_time = datetime.now()
    start_date = current_time - timedelta(weeks=2)
    end_date = current_time + timedelta(weeks=2)
    # finished_games = Game.objects.filter(is_finished=True, date_start__range=[start_date, current_time])
    # unfinished_games = Game.objects.filter(is_finished=False, date_start__range=[current_time, end_date])
    games = Game.objects.filter(Q(is_finished=False, date_start__range=[current_time, end_date]) | Q(is_finished=True, date_start__range=[start_date, current_time]))

    context = {
        'title': 'Расписание',
        'games': games,
        # 'finished_games': finished_games,
        # 'unfinished_games': unfinished_games,
    }
    return render(request, 'gameblock/shedule.html', context=context)

def ratings(request):
    player_data = Player.objects.annotate(score_count=Count('playerscore')).filter(score_count__gte=5)
    for player in player_data:
        player.games_played = player.get_games_played()
        player.average_score = player.get_average_score()
    player_data = sorted(player_data, key=lambda player: player.average_score, reverse=True)
    context = {
        'title': 'Рейтинги',
        'player_data': player_data
    }
    return render(request, 'gameblock/ratings.html', context=context)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PlayerscoreViewSet(viewsets.ModelViewSet):
    queryset = Playerscore.objects.all()
    serializer_class = PlayerscoreSerializer