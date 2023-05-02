from django.db import models

class Mensagem(models.Model):
    assunto = models.CharField(max_length=255)
    corpo = models.TextField()
    anexo = models.FileField(upload_to='anexos/', null=True, blank=True)
