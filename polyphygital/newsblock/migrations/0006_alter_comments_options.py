# Generated by Django 4.2.1 on 2023-05-13 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsblock', '0005_comments_alter_news_options_alter_news_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['time_created'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]