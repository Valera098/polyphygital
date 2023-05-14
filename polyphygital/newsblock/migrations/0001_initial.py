# Generated by Django 4.2.1 on 2023-05-12 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Категория')),
                ('discription', models.TextField(verbose_name='Описание категории')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('content', models.TextField(verbose_name='Текст новости')),
                ('image', models.ImageField(upload_to='photos', verbose_name='Фотография')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Отображение')),
                ('news_categories_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='newsblock.news_category', verbose_name='Категория')),
            ],
        ),
    ]