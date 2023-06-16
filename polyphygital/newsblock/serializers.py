from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'slug', 'news_categories_id', 'time_created', 'content', 'image', 'is_visible']

