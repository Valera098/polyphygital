# Generated by Django 4.2.1 on 2023-05-13 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameblock', '0008_alter_tournament_date_start_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='team_id',
            field=models.ManyToManyField(limit_choices_to={'id': 2}, related_name='games', to='gameblock.team', verbose_name='Участники'),
        ),
    ]
