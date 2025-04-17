from django.apps import AppConfig


class OwnAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'own_app'
