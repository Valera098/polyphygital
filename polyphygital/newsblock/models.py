from django.db import models
from django.db.models import Count
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=60, verbose_name = 'Заголовок')
    news_categories_id = models.ForeignKey('News_Category', on_delete=models.PROTECT, null=True, verbose_name = 'Категория')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата публикации')
    content = models.TextField(max_length=15000, verbose_name = 'Текст новости')
    image = models.ImageField(upload_to='photos', blank=True, verbose_name = 'Фотография')
    is_visible = models.BooleanField(default=True, verbose_name = 'Отображение')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-time_created', 'title']

class News_Category(models.Model):
    name = models.CharField(max_length=25, verbose_name = 'Категория')
    discription = models.TextField(max_length=100, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория новостей'
        verbose_name_plural = 'Категории новостей'
        ordering = ['name']