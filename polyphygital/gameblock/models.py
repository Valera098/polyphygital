from django.db import models
from django.db.models import Count

class Team(models.Model):
    name = models.CharField(max_length=16, verbose_name = 'Название команды')


