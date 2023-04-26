from django.contrib import admin
from .models import Depoimento, Nivel_Curso, Curso, Apresentacao, Pesquisa_Egresso, Rodape_links, Rodape_servico, Endereco, Slaider, Objetivos, Epregos_cerreira


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
