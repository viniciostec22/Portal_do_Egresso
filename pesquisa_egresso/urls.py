from django.urls import path
from .views import *

urlpatterns = [
    # path('pesquisa/', pesquisa, name='pesquisa'),
    path('enviar_pesquisa/', enviar_pesquisa, name='enviar_pesquisa'),
    # path('sucesso/', sucesso, name='sucesso'),
]
