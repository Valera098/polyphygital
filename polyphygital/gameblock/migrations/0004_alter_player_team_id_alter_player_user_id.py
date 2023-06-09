# Generated by Django 4.2.1 on 2023-05-12 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gameblock', '0003_alter_player_team_id_alter_player_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gameblock.team', verbose_name='ID команды'),
        ),
        migrations.AlterField(
            model_name='player',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ID игрока, как пользователя'),
        ),
    ]
