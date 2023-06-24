from rest_framework import serializers, routers
from .models import *

class NewsSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = News
        fields = ['id','title', 'slug', 'news_categories_id', 'category_name', 'get_absolute_url', 'time_created', 'content', 'image', 'is_visible']
    def get_category_name(self, obj):
        return News_Category.objects.get(id=obj.news_categories_id.id).name
    
class News_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = News_Category
        fields = ['id','name', 'discription']

class News_CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_Comment
        fields = ['id','news_id', 'user_id', 'time_created', 'content']