from django.shortcuts import render, HttpResponse
from .models import Depoimento

# Create your views here.
def Home(request):
  return render(request, 'home.html')

def Depoimentos(request):
  depoimentos = Depoimento.objects.filter(aprovado = True)
  cards = depoimentos
  return render(request, 'depoimentos.html', {'cards':cards})

def objetivos(request):
  return render(request, 'objetivos.html')

def empregos_carrera(request):
  return render(request, 'empregos.html')
