from django import forms
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
    games = Game.objects.order_by('is_finished', 'date_start')

    context = {
        'title': 'Расписание',
        'games': games,

        # 'finished_games': finished_games,
        # 'unfinished_games': unfinished_games,
    }
    return render(request, 'gameblock/shedule.html', context=context)

def ratings(request):
    player_data = Player.objects.annotate(score_count=Count('playerscore')).filter(score_count__gte=5).order_by('-score_count')
    
    context = {
        'title': 'Рейтинги',
        'player_data': player_data
    }
    
    return render(request, 'gameblock/ratings.html', context=context)


class PlayerForm(forms.ModelForm):
    team_id = forms.ModelChoiceField(queryset=Team.objects.all(), label='Команда', widget=forms.Select(attrs={'class': 'form-select'}))
    photo = forms.ImageField(label='Фото', widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    nickname = forms.CharField(label='Никнейм', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Player
        fields = ('team_id', 'photo', 'nickname',)


def create_player(request):
    if not request.user.is_authenticated:
        return redirect('homepage')
    if Player.objects.filter(user_id=request.user).exists():
        return redirect('ratings')
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            player = form.save(commit=False)
            player.user_id = request.user
            player.save()
            return redirect('ratings')
    else:
        form = PlayerForm()
    return render(request, 'gameblock/create_player.html', {'form': form})

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