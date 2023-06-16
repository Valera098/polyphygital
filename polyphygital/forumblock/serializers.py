from rest_framework import serializers, routers
from .models import *

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id','title', 'slug', 'topic_category_id', 'time_created', 'content', 'is_closed', 'user_id']

class Topic_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic_Category
        fields = ['id','name', 'discription']

class Topic_CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic_Comment
        fields = ['id','topic_id', 'user_id', 'time_created', 'content']

