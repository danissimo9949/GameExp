from django.apps import AppConfig


class GameexpAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gameexp_auth'

    def ready(self):
        import gameexp_auth.signals
        return super().ready()