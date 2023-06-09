from pyexpat import model
from django.db import models
from django import forms
from ckeditor.fields import RichTextField
from Home.models import Campi, Curso

SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    
]
ESTADO_CIVIL_CHOICES = [
    ('solteiro', 'Solteiro'),
    ('casado', 'Casado'),
    ('divorciado', 'Divorciado'),
    ('viuvo', 'Viúvo'),
]

NIVEL_ESCOLARIDADE_CHOICES = [
    ('fundamental', 'Ensino Fundamental'),
    ('medio', 'Ensino Médio'),
    ('tecnico', 'Ensino Técnico'),
    ('superior', 'Ensino Superior'),
    ('pos_graduacao', 'Pós-Graduação'),
    ('mestrado', 'Mestrado'),
    ('doutorado', 'Doutorado'),
]
AVALIACAO_APRENDIZADO_CHOICES = [
    ('ruim', 'Ruim'),
    ('media', 'Média'),
    ('bom', 'Bom'),
    ('otimo', 'Ótimo'),
]
AVALIACAO_CURSO_CHOICES = [
    ('ruim', 'Ruim'),
    ('media', 'Média'),
    ('bom', 'Bom'),
    ('otimo', 'Ótimo'),
]
class Titulo_Form(models.Model):
    titulo = RichTextField(verbose_name='titulo')
class Pesquisa(models.Model):   
    #1) Identificação 
    nome_completo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    email = models.EmailField()

    '''
    2) Caracterização dos egressos 
    2.1 Curso de Ensino concluído no IF Baiano – Campus Bom Jesus da Lapa 
    '''
    #campi = models.ForeignKey(Campi, on_delete=models.DO_NOTHING, verbose_name='Campus', blank=True, null=True)
    #curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, verbose_name="Curso", blank=True)
    curso = models.CharField(max_length=100)
    ano_conclusao = models.PositiveIntegerField(verbose_name='Ano de Conclusão')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    idade = models.PositiveIntegerField()
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL_CHOICES)
    renda_bruta = models.DecimalField(max_digits=10, decimal_places=2)
    nivel_escolaridade = models.CharField(max_length=50, choices=NIVEL_ESCOLARIDADE_CHOICES)
   

    motivo_escolha_curso = RichTextField()
    expectativas_curso = RichTextField()
    avaliacao_aprendizado = models.CharField(max_length=10,choices=AVALIACAO_APRENDIZADO_CHOICES,  verbose_name='Avaliação Aprendizado')
    avaliacao_curso = models.CharField(max_length=10,choices=AVALIACAO_CURSO_CHOICES,  verbose_name='Avaliação do Curso')
    
    participacao_pesquisa = models.BooleanField( verbose_name='Participação Projeto de Pesquisa')
    participacao_extensao = models.BooleanField(verbose_name='Participação Projeto de Extenção')
    monitor = models.BooleanField()
    realizacao_estagios = models.BooleanField(verbose_name='Realização de Estagio')
    contribuicao_monitor_estagio = RichTextField(verbose_name='Contribuição monitor estagio')
    
    #2.8 Se está fazendo ou já concluiu um curso superior, qual foi (é) o curso e em que Instituição? 
    experiencia_trabalho = RichTextField()
    trabalho_area_formacao = models.CharField(max_length=100,verbose_name='Trabalho Aréa Formação')
    situacao_atual = models.CharField(max_length=50,verbose_name='Situação Atual')
    meio_conseguir_trabalho = RichTextField()
    tipo_vinculo = models.CharField(max_length=50)

    instituicao = models.CharField(max_length=100, verbose_name='Instituição')
    

    contribuicoes_if = RichTextField(verbose_name='Contribuições do IF')
    dificuldades_curso = RichTextField()
    experiencias_if = RichTextField(verbose_name='Experiencias IF')

    sugestoes_relacao = RichTextField(verbose_name='Sugestões relação')
    sugestoes_homepage = RichTextField(verbose_name='Sugestões homepage')
    
    def __str__(self):
        return self.nome_completo
    
    
