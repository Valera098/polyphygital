from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User



class Team(models.Model):
    name = models.CharField(max_length=16, verbose_name = 'Название команды')
    logo = models.ImageField(upload_to='teamlogos', blank=True, verbose_name = 'Логотип команды')
    discription = models.TextField(max_length=2000, verbose_name = 'Описание команды')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
        ordering = ['name',]


class Discipline(models.Model):
    name = models.CharField(max_length=25, verbose_name = 'Дисциплина')
    discription = models.TextField(max_length=2000, verbose_name='Описание дисциплины')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'
        ordering = ['name']

class Player(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, verbose_name = 'ID игрока, как пользователя')
    team_id = models.ForeignKey('Team', on_delete=models.PROTECT, blank=True, null=True, verbose_name = 'Команда')
    photo = models.ImageField(upload_to='playerphotos', blank=True, verbose_name = 'Фотография')
    nickname = models.CharField(max_length=16, verbose_name = 'Никнейм')

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'
        ordering = ['id']

class Tournament(models.Model):
    title = models.CharField(max_length=25, verbose_name='Название турнира')
    discription = models.TextField(max_length=2000, verbose_name='Описание турнира')
    team_id = models.ManyToManyField('Team', blank=True, verbose_name='Участники', related_name='tournaments')
    date_start = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата окончания', blank=True, null=True)
    is_finished = models.BooleanField(default=False, verbose_name='Оконченность')
    winner_id = models.ForeignKey('Team', on_delete=models.PROTECT, blank=True, null=True,  verbose_name='Победитель', related_name='won_tournaments')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
        ordering = ['id']

class Game(models.Model):
    tournament_id = models.ForeignKey('Tournament', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Турнир')
    discipline_id = models.ForeignKey('Discipline', on_delete=models.PROTECT, blank=False, null=False, verbose_name='Дисциплина')
    date_start = date_start = models.DateTimeField(verbose_name='Время начала')
    team_id = models.ManyToManyField('Team', verbose_name='Участники', related_name='games')
    is_finished = models.BooleanField(default=False, verbose_name='Оконченность')
    winner_id = models.ForeignKey('Team', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Победитель',related_name='won_games')

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['id']

    def __str__(self):
        return f"{self.discipline_id.name} ({datetime.strftime(self.date_start, '%d.%m.%Y %H:%M')}) - ID: {self.id}"

class Playerscore(models.Model):
    player_id = models.ForeignKey('Player', on_delete=models.PROTECT, verbose_name='Игрок')
    game_id = models.ForeignKey('Game', on_delete=models.PROTECT, verbose_name='Игра')
    score = models.IntegerField(verbose_name='Очки')

    class Meta:
        verbose_name = 'Очки'
        verbose_name_plural = 'Очки'
        ordering = ['-id']
