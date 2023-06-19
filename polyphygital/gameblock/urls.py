from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'teams', TeamViewSet)
router.register(r'disciplines', DisciplineViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'tournaments', TournamentViewSet)
router.register(r'games', GameViewSet)
router.register(r'playerscores', PlayerscoreViewSet)

# urlpatterns = [
#     path('shedule/', shedule, name = 'shedule'),
#     path('ratings/', ratings, name = 'ratings' ),
# ]

urlpatterns = [
    path('api/', include(router.urls)),
]