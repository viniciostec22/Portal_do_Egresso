from django.contrib import admin
from .models import *


class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso','turma', 'data_criacao', 'depoimento', 'aprovado')
    list_filter = ('aprovado',)
    list_editable = ('aprovado',)
    list_display_links = ('nome',)

admin.site.register(Depoimento, DepoimentoAdmin)
admin.site.register(Nivel_Curso)
admin.site.register(Curso)
admin.site.register(Apresentacao)
admin.site.register(Pesquisa_Egresso)
admin.site.register(Rodape_links)
admin.site.register(Rodape_servico)
admin.site.register(Endereco)
admin.site.register(Slaider)
admin.site.register(Objetivos)
admin.site.register(Epregos_cerreira)
admin.site.register(Campi)

