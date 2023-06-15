from django.db import models
from django.db.models import Count
from django.urls import reverse
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=60, verbose_name = 'Заголовок новости')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    news_categories_id = models.ForeignKey('News_Category', on_delete=models.CASCADE, null=True, verbose_name = 'Категория новости')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата публикации')
    content = models.TextField(max_length=15000, verbose_name = 'Текст новости')
    image = models.ImageField(upload_to='photos', blank=True, verbose_name = 'Фотография')
    is_visible = models.BooleanField(default=True, verbose_name='Отображение')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-time_created', 'title']

class News_Category(models.Model):
    name = models.CharField(max_length=25, verbose_name = 'Категория новости')
    discription = models.TextField(max_length=100, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория новостей'
        verbose_name_plural = 'Категории новостей'
        ordering = ['name']

class Comments(models.Model):
    news_id = models.ForeignKey(News, on_delete=models.PROTECT, verbose_name='Новость')
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    content = models.TextField(max_length=350, verbose_name='Текст комментария')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['time_created']

