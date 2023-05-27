from django.contrib import admin

from .models import *

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id','news_id', 'time_created',)
    list_display_links = ('id', 'time_created',)
    search_fields = ('id',)
    ordering = ('time_created',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'news_category', 'time_created', 'is_visible',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    ordering = ('-time_created', 'title')
    prepopulated_fields = {"slug": ("title",)}

    def news_category(self, obj):
        return obj.news_categories_id.name

class News_CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'news_count')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    ordering = ('id', )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(news_count=Count('news'))
        return queryset

    def news_count(self, obj):
        return obj.news_count

    news_count.short_description = 'Количество новостей'

admin.site.register(News, NewsAdmin)
admin.site.register(News_Category, News_CategoryAdmin)
admin.site.register(Comments, CommentsAdmin)