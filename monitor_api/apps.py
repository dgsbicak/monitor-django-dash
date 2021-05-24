from django.apps import AppConfig

class MonitorApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monitor_api'

    def ready(self):
        from monitor_api.utils import signals
