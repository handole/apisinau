from django.apps import AppConfig


class SinauConfig(AppConfig):
    name = 'sinau'

    def ready(self) -> None:
        from . import signals
        
