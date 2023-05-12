from django.apps import AppConfig


class NewsblockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsblock'
    verbose_name = 'Новостной блок'

class GameblockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gameblock'
    verbose_name = 'Игровой блок'
