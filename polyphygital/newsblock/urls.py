from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name = 'homepage'),
    path('news/', news, name = 'newspage'),
    path('news/post/<slug:post_slug>', show_post, name='post'),
    path('register/', RegisterUser.as_view(), name = 'register'),
    path('login/', LoginUser.as_view(), name = 'login'),
    path('logout/', logout_user, name='logout'),
]