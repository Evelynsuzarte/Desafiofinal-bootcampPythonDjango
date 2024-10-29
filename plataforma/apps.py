from django.apps import AppConfig


class PlataformaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'plataforma'
class PlataformaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'plataforma'

    def ready(self):
        print("Iniciando configuração da plataforma...")
        from .scripts.setup_inicial import setup_inicial
        setup_inicial()
