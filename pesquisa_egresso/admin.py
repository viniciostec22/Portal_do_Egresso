from django.contrib import admin
from .models import Pesquisa, Titulo_Form

@admin.register(Pesquisa)
class PesquisaAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'telefone', 'email')

admin.site.register(Titulo_Form)