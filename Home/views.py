from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def Home(request):
  if request.method == 'GET':
    apresentacao = Apresentacao.objects.all().first()
    pesquisa_egresso = Pesquisa_Egresso.objects.all().first()
    links = Rodape_links.objects.all()
    servicos = Rodape_servico.objects.all()
    endereco = Endereco.objects.all().first()
    slaider = Slaider.objects.all()
    campi = Campi.objects.all()
    
    return render(request, 'home.html', {'apresentacao':apresentacao, 
                                        'pesquisa_egresso':pesquisa_egresso, 
                                        'links':links, 
                                        'servicos':servicos,
                                        'endereco':endereco,
                                        'slaider':slaider,
                                        'campi':campi,
                                        })
  elif request.method == 'POST':
      nome = request.POST.get('nome')
      email = request.POST.get('email')
      telefone = request.POST.get('telefone')
      aceito = request.POST.get('aceito')
      politica = request.POST.get('politica')
      
      if aceito != '1':
          messages.add_message(request, constants.ERROR, 'Você precisa Autorizar o recebimento de conteudos.')
          return redirect('depoimentos')
      else:
          aceito = True

      if politica != '1':
            messages.add_message(request, constants.ERROR, 'Você precisa aceitar os termos e condições.')
            return redirect('depoimentos')
      else:
          politica = True
          
      if not nome:
          messages.add_message(request, constants.ERROR, 'Por favor, informe seu nome.')
      elif not email:
          messages.add_message(request, constants.ERROR, 'Por favor, informe seu e-mail.')
      elif not telefone:
          messages.add_message(request, constants.ERROR, 'Por favor, informe seu telefone.')
      else:
          novo_contato = Contato(
            nome=nome,
            email=email,
            telefone=telefone,
            enviado_boas_vindas=False # define o campo que indica se o e-mail de boas-vindas já foi enviado
          )
         
          
          # Envia o e-mail de boas-vindas para o novo contato
          context = {'novo_contato': novo_contato}
          html_content = render_to_string('email/boas_vindas_newslatter.html', context)
          text_content = strip_tags(html_content)
      
          email = EmailMultiAlternatives(
            'Bem-vindo à nossa newsletter', 
            text_content, 
            settings.EMAIL_HOST_USER, 
            [email]
          )
          email.attach_alternative(html_content, 'text/html')
          email.send()
          
          
          novo_contato.enviado_boas_vindas = True
          novo_contato.save()
          messages.add_message(request, constants.SUCCESS, 'Contato enviado com sucesso!!')
          return redirect('home')

    
def cursos_do_campus(request, campus_id):
    cursos = Curso.objects.filter(campus__id=campus_id)
    cursos_list = [{'id': curso.id, 'nome': curso.curso, 'nivel': curso.nivel.nivel_curso  } for curso in cursos] # type: ignore
    #print(cursos_list)
    return JsonResponse({'cursos': cursos_list})
  
def Depoimentos(request):
  search = request.GET.get('search', '')
  links = Rodape_links.objects.all()
  servicos = Rodape_servico.objects.all()
  endereco = Endereco.objects.all().first()
  nivel_curso = Nivel_Curso.objects.all()
  cursos = Curso.objects.all()
  campi = Campi.objects.all()
  cards_list = Depoimento.objects.filter(aprovado=True).filter(
                                      Q(campus__nome_campus__contains=search)|
                                      Q(curso__curso__contains=search) |
                                      Q(turma__contains=search) | 
                                      Q(curso__nivel__nivel_curso__contains=search))
  paginator = Paginator(cards_list, 4) # 4 cards por página
  page = request.GET.get('page')
  cards = paginator.get_page(page) 
  print(cards_list)
   
  return render(request, 'depoimentos.html', {'cards':cards, 
                                                'nivel_curso':nivel_curso, 
                                                'cursos':cursos,
                                                'campi':campi, 
                                                'links':links, 
                                                'servicos':servicos,
                                                'endereco':endereco,
                                                })
  
    
def add_depoimentos(request):
  if request.method =='POST':
      nome = request.POST.get('nome')
      email = request.POST.get('email')
      foto = request.FILES.get('foto')
      #nivel = request.POST.get('nivel')
      turma = request.POST.get('turma')
      campus = request.POST.get('campus')
      curso = request.POST.get('curso')
      depoimento = request.POST.get('depoimento')
      autorizacao_publicacao = request.POST.get('autorizacao')  
      aceite_politica_privacidade = request.POST.get('politica_privacidade')       
      if not nome:
          messages.add_message(request, constants.ERROR, 'O campo Nome é obrigatório.')
          return redirect('depoimentos')
      elif not email:
          messages.add_message(request, constants.ERROR, 'O campo E-mail é obrigatório.')
          return redirect('depoimentos')
      elif not turma:
          messages.add_message(request, constants.ERROR, 'O campo Turma é obrigatório.')
          return redirect('depoimentos')
      elif not campus:
          messages.add_message(request, constants.ERROR, 'O campo Campus é obrigatório.')
          return redirect('depoimentos')
      elif not curso:
          messages.add_message(request, constants.ERROR, 'O campo Curso é obrigatório.')
          return redirect('depoimentos')
      elif not depoimento:
          messages.add_message(request, constants.ERROR, 'O campo Depoimento é obrigatório.')
          return redirect('depoimentos')

      #validação termos 
      if autorizacao_publicacao != '1':
        messages.add_message(request, constants.ERROR, 'Você precisa aceitar os termos e condições.')
        return redirect('depoimentos')
      else:
        autorizacao_publicacao = True

      if aceite_politica_privacidade != '1':
          messages.add_message(request, constants.ERROR, 'Você precisa aceitar os termos e condições.')
          return redirect('depoimentos')
      else:
        aceite_politica_privacidade = True
      #Cria uma instância do modelo Depoimento com os dados recebidos
      novo_depoimento = Depoimento(
          nome=nome,
          email=email,
          foto=foto,
          #nivel_id= curso.nivel,
          campus_id = campus,
          turma=turma,
          curso_id=curso,
          depoimento=depoimento,
          autorizacao_publicacao=autorizacao_publicacao,
          aceite_politica_privacidade=aceite_politica_privacidade
      )
      # Salva o novo depoimento no banco de dados
      novo_depoimento.save()
      messages.add_message(request, constants.SUCCESS, 'Depoimento enviado com sucesso!!')
      # Redireciona o usuário para uma página de sucesso ou para a página de depoimentos
      return redirect('depoimentos')  
    
        
def politica_privacidade(request):
  politica = Politica.objects.get(id=1) # obtém o primeiro objeto da model Politica
  pdf_path = politica.arquivo.path
  with open(pdf_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=politica.pdf'
        return response
  
  #return render(request, 'politica.html', {'politica': politica})
  
def objetivos(request):
  objetivo = Objetivos.objects.all().first
  links = Rodape_links.objects.all()
  servicos = Rodape_servico.objects.all()
  endereco = Endereco.objects.all().first()
  
  return render(request, 'objetivos.html', { 'links':links, 
                                             'servicos':servicos,
                                             'endereco':endereco,
                                             'objetivo':objetivo,
                                             })

def empregos_carrera(request):
  links = Rodape_links.objects.all()
  servicos = Rodape_servico.objects.all()
  endereco = Endereco.objects.all().first()
  empregos_carrera = Epregos_cerreira.objects.first()
  return render(request, 'empregos.html',{ 'links':links, 
                                             'servicos':servicos,
                                             'endereco':endereco,
                                             'empregos_carrera':empregos_carrera,
                                             })
