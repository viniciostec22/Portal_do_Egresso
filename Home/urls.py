from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('depoimentos/', views.Depoimentos, name='depoimentos'),
    path('objetivos/', views.objetivos, name='objetivos')
]
