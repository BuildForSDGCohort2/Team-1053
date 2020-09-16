from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'api.orders'

    def ready(self):
        from . import signals  # noqa
