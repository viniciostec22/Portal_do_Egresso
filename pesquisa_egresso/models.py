from django.db import models

from Home.models import Endereco

class Pesquisa(models.Model):
    nome_completo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    email = models.EmailField()

    curso = models.CharField(max_length=100)
    ano_conclusao = models.PositiveIntegerField(verbose_name='Ano de Conclusão')
    sexo = models.CharField(max_length=10)
    idade = models.PositiveIntegerField()
    estado_civil = models.CharField(max_length=20)
    renda_bruta = models.DecimalField(max_digits=10, decimal_places=2)
    nivel_escolaridade = models.CharField(max_length=50)
    curso_superior = models.CharField(max_length=100)

    motivo_escolha_curso = models.TextField()
    expectativas_curso = models.TextField()
    avaliacao_aprendizado = models.PositiveIntegerField(verbose_name='Avaliação Aprendizado')
    avaliacao_curso = models.PositiveIntegerField(verbose_name='Avaliação Curso')
    participacao_pesquisa = models.BooleanField( verbose_name='Participação Projeto de Pesquisa')
    participacao_extensao = models.BooleanField(verbose_name='Participação Projeto de Extenção')
    monitor = models.BooleanField()
    realizacao_estagios = models.BooleanField(verbose_name='Realização de Estagio')
    contribuicao_monitor_estagio = models.TextField(verbose_name='Contribuição monitor estagio')

    experiencia_trabalho = models.TextField()
    trabalho_area_formacao = models.CharField(max_length=100,verbose_name='Trabalho Aréa Formação')
    situacao_atual = models.CharField(max_length=50)
    meio_conseguir_trabalho = models.TextField()
    tipo_vinculo = models.CharField(max_length=50)

    instituicao = models.CharField(max_length=100, verbose_name='Instituição')
    nome_curso = models.CharField(max_length=100)

    contribuicoes_if = models.TextField()
    dificuldades_curso = models.TextField()
    experiencias_if = models.TextField(verbose_name='Experiencias IF')

    sugestoes_relacao = models.TextField(verbose_name='Sugestões relação')
    sugestoes_homepage = models.TextField(verbose_name='Sugestões homepage')
    
    def __str__(self):
        return self.nome_completo
    
    
