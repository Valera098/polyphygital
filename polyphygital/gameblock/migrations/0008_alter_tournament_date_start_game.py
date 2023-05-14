# Generated by Django 4.2.1 on 2023-05-13 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameblock', '0007_alter_tournament_date_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='date_start',
            field=models.DateField(verbose_name='Дата начала'),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(verbose_name='Время начала')),
                ('is_finished', models.BooleanField(default=False, verbose_name='Оконченность')),
                ('discipline_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gameblock.discipline', verbose_name='Дисциплина')),
                ('team_id', models.ManyToManyField(blank=True, related_name='games', to='gameblock.team', verbose_name='Участники')),
                ('tournament_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gameblock.tournament', verbose_name='Турнир')),
                ('winner_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='won_games', to='gameblock.team', verbose_name='Победитель')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
                'ordering': ['id'],
            },
        ),
    ]