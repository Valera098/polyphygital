from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name = 'homepage'),
    path('news/', news, name = 'newspage'),
    path('news/post/<int:post_id>', show_post, name='post'),
]