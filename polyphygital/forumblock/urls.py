from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'topics', TopicViewSet)
router.register(r'topic-categories', Topic_CategoryViewSet)
router.register(r'topic-comments', Topic_CommentViewSet)

urlpatterns = [
    path('forum/', forum, name='forum'),
    path('forum/newthread', new_thread, name='newthread'),
    path('forum/thread/<slug:thread_slug>', show_thread, name='thread'),
    path('api/', include(router.urls)),
]