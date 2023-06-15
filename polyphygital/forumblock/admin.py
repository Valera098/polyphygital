from django.contrib import admin

from .models import *
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'topic_category', 'time_created', 'is_closed',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    ordering = ('-time_created', 'title')
    prepopulated_fields = {"slug": ("title",)}

    def topic_category(self, obj):
        return obj.topic_category_id.name

class Topic_CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'topic_count')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    ordering = ('id', )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(topic_count=Count('topic'))
        return queryset

    def topic_count(self, obj):
        return obj.topic_count

    topic_count.short_description = 'Количество обсуждений'

class Topic_CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id','topic_id', 'time_created',)
    list_display_links = ('id', 'time_created',)
    search_fields = ('id',)
    ordering = ('time_created',)

admin.site.register(Topic, TopicAdmin)
admin.site.register(Topic_Category, Topic_CategoryAdmin)
admin.site.register(Topic_Comment, Topic_CommentAdmin)