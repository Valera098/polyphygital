# Generated by Django 4.2.1 on 2023-05-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsblock', '0003_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos', verbose_name='Фотография'),
        ),
    ]
