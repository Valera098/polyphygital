# Generated by Django 4.2.1 on 2023-05-12 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameblock', '0005_alter_player_options_alter_discipline_discription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='title',
            field=models.CharField(max_length=25, verbose_name='Название турнира'),
        ),
    ]
