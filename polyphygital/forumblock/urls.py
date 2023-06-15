from django.urls import path

from .views import *

urlpatterns = [
    path('forum/', forum, name='forum'),
    path('forum/newthread', new_thread, name='newthread'),
    path('forum/thread/<slug:thread_slug>', show_thread, name='thread'),
]