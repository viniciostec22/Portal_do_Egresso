from pyexpat import model
from django.shortcuts import render, redirect
from .models import Depoimento, Nivel_Curso, Curso, Apresentacao, Pesquisa_Egresso, Rodape_links, Rodape_servico, Endereco, Slaider, Objetivos, Epregos_cerreira
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
def Home(request):
  apresentacao = Apresentacao.objects.all().first()
  pesquisa_egresso = Pesquisa_Egresso.objects.all().first()
  links = Rodape_links.objects.all()
  servicos = Rodape_servico.objects.all()
  endereco = Endereco.objects.all().first()
  slaider = Slaider.objects.all()
  return render(request, 'home.html', {'apresentacao':apresentacao, 
                                       'pesquisa_egresso':pesquisa_egresso, 
                                       'links':links, 
                                       'servicos':servicos,
                                       'endereco':endereco,
                                       'slaider':slaider,
                                       })

def Depoimentos(request):
  links = Rodape_links.objects.all()
  servicos = Rodape_servico.objects.all()
  endereco = Endereco.objects.all().first()
  nivel_curso = Nivel_Curso.objects.all()
  cursos = Curso.objects.all()
  depoimentos = Depoimento.objects.filter(aprovado = True)
  cards = depoimentos
  if request.method == 'GET':
    return render(request, 'depoimentos.html', {'cards':cards, 
                                                'nivel_curso':nivel_curso, 
                                                'cursos':cursos, 
                                                'links':links, 
                                                'servicos':servicos,
                                                'endereco':endereco,})
  
  elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        foto = request.FILES.get('foto')
        nivel = request.POST.get('nivel')
        turma = request.POST.get('turma')
        curso = request.POST.get('curso')
        depoimento = request.POST.get('depoimento')
        autorizacao_publicacao = request.POST.get('autorizacao')  
        aceite_politica_privacidade = request.POST.get('politica_privacidade')       

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
            nivel_id=nivel,
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
    
# def novo_depoimento(request):
#   nivel_curso = Nivel_Curso.objects.all()
#   curso = Curso.objects.all()
#   if request.method == 'GET':
#     return render(request, 'depoimentos.html', {'nivel_curso':nivel_curso, 'curso':curso})
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
