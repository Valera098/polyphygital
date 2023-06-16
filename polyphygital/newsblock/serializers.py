from rest_framework import serializers, routers
from .models import *

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id','title', 'slug', 'news_categories_id', 'time_created', 'content', 'image', 'is_visible']

class News_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = News_Category
        fields = ['id','name', 'discription']

class News_CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_Comment
        fields = ['id','news_id', 'user_id', 'time_created', 'content']