from rest_framework import serializers, routers
from .models import *

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'logo', 'discription']

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = ['id', 'name', 'discription']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'user_id', 'team_id', 'photo', 'nickname']

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'title', 'discription', 'team_id', 'date_start', 'date_end', 'is_finished', 'winner_id']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'tournament_id', 'discipline_id', 'date_start', 'team_id', 'is_finished', 'winner_id']

class PlayerscoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playerscore
        fields = ['id', 'player_id', 'game_id', 'score']