from django.apps import AppConfig


class BaseConfig(AppConfig):
    verbose_name ='Modulo Geral'
    default_auto_field ='django.db.models.BigAutoField'
    name = 'base'
    verbose_name = 'Módulo de Eventos'