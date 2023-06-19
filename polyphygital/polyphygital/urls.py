from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include

from newsblock.views import *
from polyphygital import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('newsblock.urls')),
    # path('', include('gameblock.urls')),
    # path('', include('forumblock.urls')),
    path('', include('newsblock.urls')),
    path('', include('gameblock.urls')),
    path('', include('forumblock.urls')),
    path('', include('frontend_helper.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
