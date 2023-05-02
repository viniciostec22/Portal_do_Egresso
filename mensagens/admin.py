from django.contrib import admin
from .models import Mensagem

class MensagemAdmin(admin.ModelAdmin):
    list_display = ['assunto']
    search_fields = ['assunto']

admin.site.register(Mensagem, MensagemAdmin)
