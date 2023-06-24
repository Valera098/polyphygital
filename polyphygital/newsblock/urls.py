from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'news', NewsViewSet)
router.register(r'news-categories', News_CategoryViewSet)
router.register(r'news-comments', News_CommentViewSet)

urlpatterns = [
    path('', index, name = 'homepage'),
    path('news/', news, name = 'newspage'),
    path('news/post/<slug:post_slug>', show_post, name='post'),
    path('register/', RegisterUser.as_view(), name = 'register'),
    path('login/', LoginUser.as_view(), name = 'login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('delete-player-self/', delete_player_self, name='delete-player-self'),
    path('api/', include(router.urls)),
]