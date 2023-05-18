from pyexpat import model
from django.shortcuts import render, redirect
from .forms import PesquisaForm
from django.contrib import messages
from django.contrib.messages import constants
from .models import Titulo_Form
from Home.models import Rodape_servico, Rodape_links, Endereco, Campi
# def pesquisa(request):
#     form = PesquisaForm()
#     return render(request, 'form_pesquisa.html', {'form': form})

def enviar_pesquisa(request):
    links = Rodape_links.objects.all()
    servicos = Rodape_servico.objects.all()
    endereco = Endereco.objects.all().first()
    campus = Campi.objects.all()
    if request.method == 'GET':
        form = PesquisaForm()
        titulo = Titulo_Form.objects.first()
        return render(request, 'form_pesquisa.html', {'form': form, 
                                                      'titulo':titulo,
                                                      'links':links, 
                                                      'campus':campus,
                                                      'servicos':servicos,
                                                      'endereco':endereco,})
    elif request.method == 'POST':
        form = PesquisaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Pesquisa enviada com sucesso!!')
            return redirect('home')
    else:
        form = PesquisaForm()
    return render(request, 'form_pesquisa.html', {'form': form})

# def sucesso(request):
#     return render(request, 'sucesso.html')
