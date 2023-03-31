import email
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.forms import CharField

class Nivel_Curso(models.Model):
  nivel_curso = models.CharField(max_length=50)
  
  def __str__(self) -> str:
    return self.nivel_curso
  
class Curso(models.Model):
  curso = models.CharField(max_length=50)
  
  def __str__(self) -> str:
    return self.curso
  
class Depoimento(models.Model):
  nome = models.CharField(max_length=50)
  email = models.EmailField(max_length=254)
  foto = models.ImageField(upload_to='img_perfil', blank=True, null=True)
  nivel = models.ForeignKey(Nivel_Curso, on_delete=models.DO_NOTHING) 
  turma = models.CharField(max_length=20)
  curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
  depoimento = models.TextField()
  autorizacao_publicacao = models.BooleanField(default=False)
  aceite_politica_privacidade = models.BooleanField(default=False)
  aprovado = models.BooleanField(default=False)
  data_criacao = models.DateTimeField(auto_now_add=True)
  
  def __str__(self) -> str:
    return self.nome