from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request):
  return render(request, 'home.html')

def Depoimentos(request):
  cards = [1,2,3,4]
  return render(request, 'depoimentos.html', {'cards':cards})

def objetivos(request):
  return render(request, 'objetivos.html')

def empregos_carrera(request):
  return render(request, 'empregos.html')
