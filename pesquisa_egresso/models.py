from django.db import models

class Pesquisa(models.Model):
    nome_completo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    email = models.EmailField()

    curso = models.CharField(max_length=100)
    ano_conclusao = models.PositiveIntegerField()
    sexo = models.CharField(max_length=10)
    idade = models.PositiveIntegerField()
    estado_civil = models.CharField(max_length=20)
    renda_bruta = models.DecimalField(max_digits=10, decimal_places=2)
    nivel_escolaridade = models.CharField(max_length=50)
    curso_superior = models.CharField(max_length=100)

    motivo_escolha_curso = models.TextField()
    expectativas_curso = models.TextField()
    avaliacao_aprendizado = models.PositiveIntegerField()
    avaliacao_curso = models.PositiveIntegerField()
    participacao_pesquisa = models.BooleanField()
    participacao_extensao = models.BooleanField()
    monitor = models.BooleanField()
    realizacao_estagios = models.BooleanField()
    contribuicao_monitor_estagio = models.TextField()

    experiencia_trabalho = models.TextField()
    trabalho_area_formacao = models.CharField(max_length=100)
    situacao_atual = models.CharField(max_length=50)
    meio_conseguir_trabalho = models.TextField()
    tipo_vinculo = models.CharField(max_length=50)

    instituicao = models.CharField(max_length=100)
    nome_curso = models.CharField(max_length=100)

    contribuicoes_if = models.TextField()
    dificuldades_curso = models.TextField()
    experiencias_if = models.TextField()

    sugestoes_relacao = models.TextField()
    sugestoes_homepage = models.TextField()
    
    def __str__(self):
        return self.nome_completo
    
    
