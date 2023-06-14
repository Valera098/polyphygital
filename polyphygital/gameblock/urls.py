from django.urls import path

from .views import *

urlpatterns = [
    path('shedule/', shedule, name = 'shedule'),
    path('ratings/', ratings, name = 'ratings' )
]