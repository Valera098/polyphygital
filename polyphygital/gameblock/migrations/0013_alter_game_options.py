# Generated by Django 4.2.1 on 2023-06-14 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameblock', '0012_alter_game_team_id_playerscore'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['date_start'], 'verbose_name': 'Игра', 'verbose_name_plural': 'Игры'},
        ),
    ]