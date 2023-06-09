import email
from django.db import models
from PIL import Image
from django.db import models
from ckeditor.fields import RichTextField


class Contato(models.Model):
  nome = models.CharField(max_length=100, verbose_name="Nome")
  email = models.EmailField(verbose_name="E-mail")
  telefone = models.CharField(max_length=11, verbose_name="Telefone")
  enviado_boas_vindas = models.BooleanField(default=False,verbose_name="Email de confirmação")
  
  def __str__(self) -> str:
     return self.nome

class Nivel_Curso(models.Model):
    nivel_curso = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nivel_curso

class Campi(models.Model):
    nome_campus = models.CharField(max_length=50, verbose_name="Campus")
    cidade = models.CharField(max_length=50, verbose_name="Cidade")
    endereco = models.CharField(max_length=150, verbose_name="Endereço")

    def __str__(self) -> str:
        return self.nome_campus

class Curso(models.Model):
    curso = models.CharField(max_length=50)
    descricao = RichTextField(null=True)
    campus = models.ManyToManyField(Campi, related_name='cursos')
    nivel = models.ForeignKey(Nivel_Curso, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.curso
  
class Depoimento(models.Model):
  nome = models.CharField(max_length=50)
  email = models.EmailField(max_length=254)
  foto = models.ImageField(upload_to='img_perfil/', blank=True, null=True)
  #nivel = models.ForeignKey(Nivel_Curso, on_delete=models.DO_NOTHING, null=True) 
  turma = models.CharField(max_length=20)
  campus = models.ForeignKey(Campi, on_delete=models.DO_NOTHING, null=True)
  curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
  depoimento = RichTextField()
  autorizacao_publicacao = models.BooleanField(default=False)
  aceite_politica_privacidade = models.BooleanField(default=False)
  aprovado = models.BooleanField(default=False)
  data_criacao = models.DateTimeField(auto_now_add=True)
  
  def __str__(self) -> str:
    return self.nome
  
class Slaider(models.Model):
    img = models.ImageField(upload_to='img/')
    btn = models.CharField(max_length=50, verbose_name='Nome do Botão', blank=True, null=True)
    url_btn = models.CharField(max_length=200, verbose_name='Link do Banner',blank=True, null=True)
    titulo_banner = RichTextField(verbose_name='Titulo Banner',blank=True, null=True)
    texto_banner = RichTextField(verbose_name='Paragrafo Banner',blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Abre a imagem usando a biblioteca Pillow
        with Image.open(self.img.path) as img:
            # Verifica se a imagem é maior do que 800px de largura
            if img.width > 1200:
                # Redimensiona a imagem para 800px de largura mantendo a proporção
                img.thumbnail((1200, 1200))

                # Sobrescreve a imagem original com a imagem redimensionada
                img.save(self.img.path)
    def __str__(self) -> str:
      return self.img.url
    
  
class Apresentacao(models.Model):
  titulo = models.CharField(max_length=15)
  texto_esquerdo =RichTextField( verbose_name="Texto esquerda")
  texto_direita = RichTextField(verbose_name="texto direita")
    
  def __str__(self) -> str:
    return self.titulo
  
class Pesquisa_Egresso(models.Model):
  titulo = models.CharField(max_length=30)
  texto = RichTextField(verbose_name="texto")
  subtitulo=models.CharField(max_length=30, verbose_name="Subtitulo")
  texto_direita = RichTextField(verbose_name="texto direita")
  def __str__(self) -> str:
    return self.titulo
  
# class Cadastro(models.Model):
#    nome = models.CharField(max_length=50, verbose_name="Nome")
#    email = models.EmailField(max_length=254) 
#    turma = models.CharField(max_length=20)
  
class Rodape_links(models.Model):
  nome_link = models.CharField(max_length=30, verbose_name="Nome do Link", null=True)
  links_importantes = models.CharField(max_length=200 ,verbose_name="URL")
  def __str__(self) -> str:
    return self.nome_link # type: ignore
  
class Rodape_servico(models.Model):
  servicos = models.CharField(max_length=150,verbose_name="Serviços")
  link_servico = models.CharField(max_length=200 ,verbose_name="URL serviço",  null=True)
  def __str__(self) -> str:
    return self.servicos
class Endereco(models.Model):
  endereco = RichTextField(verbose_name="Endereço")
  def __str__(self) -> str:
    return self.endereco
  
  #objetivos
  
class Objetivos(models.Model):
  titulo = models.CharField(max_length=40, verbose_name="Titulo pagina de Objetivo")
  texto = RichTextField(verbose_name="Texto da descrição do objetivo")
  def __str__(self) -> str:
    return self.titulo
  
class Epregos_cerreira(models.Model):
  titulo = models.CharField(max_length=40, verbose_name="Titulo pagina Empregos e carreiras")
  texto = RichTextField(verbose_name="Texto da descrição ")
  def __str__(self) -> str:
    return self.titulo
  
class Politica(models.Model):
    titulo = models.CharField(max_length=100)
    politica = RichTextField(verbose_name='Politica de Privacidade', blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
      
      
class Mensagem(models.Model):
    assunto = models.CharField(max_length=255)
    corpo = RichTextField()
    anexo = models.FileField(upload_to='anexos/', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.assunto