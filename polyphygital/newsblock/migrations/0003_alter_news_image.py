# Generated by Django 4.2.1 on 2023-05-12 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsblock', '0002_alter_news_options_alter_news_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to='photos', verbose_name='Фотография'),
        ),
    ]
