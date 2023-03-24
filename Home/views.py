from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request):
  return render(request, 'home.html')

def Depoimentos(request):
  return render(request, 'depoimentos.html')