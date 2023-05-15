from django.shortcuts import render, redirect
from .forms import PesquisaForm
from django.contrib import messages
from django.contrib.messages import constants

# def pesquisa(request):
#     form = PesquisaForm()
#     return render(request, 'form_pesquisa.html', {'form': form})

def enviar_pesquisa(request):
    if request.method == 'GET':
        form = PesquisaForm()
        return render(request, 'form_pesquisa.html', {'form': form})
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
