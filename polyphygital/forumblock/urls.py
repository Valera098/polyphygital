from django.urls import path

from .views import *

urlpatterns = [
    path('forum/', forum, name='forum'),
]