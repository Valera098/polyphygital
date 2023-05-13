from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import *

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'num_players')
    list_display_links = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

    def num_players(self, obj):
        return Player.objects.filter(team_id=obj).count()

    num_players.short_description = 'Количество игроков'

class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'num_games')
    list_display_links = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(num_games=Count('game'))
        return queryset

    def num_games(self, obj):
        return obj.num_games

    num_games.short_description = 'Количество игр'

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'team_id', 'user_id',)
    list_display_links = ('nickname',)
    search_fields = ('nickname',)
    ordering = ('team_id', 'nickname')

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_start', 'date_end', 'is_finished', 'winner_id')
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    ordering = ('-date_start', 'title')

    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple(verbose_name='Команды', is_stacked=False)}
    }

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

    def clean_team_id(self):
        teams = self.cleaned_data['team_id']
        if len(teams) != 2:
            raise ValidationError('Можно выбрать только ровно две команды')
        return teams


class GameAdmin(admin.ModelAdmin):
    form = GameForm
    list_display = ('id', 'tournament_id', 'discipline_id', 'date_start', 'is_finished', 'winner_id')
    list_display_links = ('id', 'tournament_id',)
    search_fields = ('',)
    ordering = ('-date_start', 'id')

    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple(verbose_name='Команды', is_stacked=False)}
    }

class PlayerscoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'player_id', 'game_id', 'score')
    list_display_links = ('id',)
    search_fields = ('',)
    ordering = ('-id',)


admin.site.register(Team, TeamAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Playerscore, PlayerscoreAdmin)
