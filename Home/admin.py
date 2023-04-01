from django.contrib import admin
from .models import *


class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'data_criacao', 'depoimento', 'aprovado')
    list_filter = ('aprovado',)
    list_editable = ('aprovado',)
    list_display_links = ('nome',)

admin.site.register(Depoimento, DepoimentoAdmin)
admin.site.register(Nivel_Curso)
admin.site.register(Curso)