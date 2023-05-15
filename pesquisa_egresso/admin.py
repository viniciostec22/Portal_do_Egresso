from django.contrib import admin
from .models import Pesquisa

@admin.register(Pesquisa)
class PesquisaAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'telefone', 'email')
