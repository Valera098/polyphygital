from django.db import models
from django.db.models import Count
from django.urls import reverse
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=60, verbose_name = 'Заголовок обсуждения')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    topic_category_id = models.ForeignKey('Topic_Category', on_delete=models.CASCADE, null=True, verbose_name = 'Категория обсуждения')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата публикации')
    content = models.TextField(max_length=15000, verbose_name = 'Текст обсуждения')
    is_closed = models.BooleanField(default=False, verbose_name='Отображение')
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False, verbose_name = 'ID создателя обсуждения')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('thread', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Обсуждение'
        verbose_name_plural = 'Обсуждения'
        ordering = ['-time_created', 'title']

class Topic_Category(models.Model):
    name = models.CharField(max_length=25, verbose_name = 'Категория обсуждения')
    discription = models.TextField(max_length=100, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория обсуждения'
        verbose_name_plural = 'Категории обсуждения'
        ordering = ['name']

class Topic_Comment(models.Model):
    topic_id = models.ForeignKey(Topic, on_delete=models.PROTECT, verbose_name='Обсуждение')
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    content = models.TextField(max_length=350, verbose_name='Текст комментария')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['time_created']