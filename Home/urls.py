from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('depoimentos/', views.Depoimentos, name='depoimentos'),
    path('new_depoimento', views.add_depoimentos, name='new_depoimento'),
    path('objetivos/', views.objetivos, name='objetivos'),
    path('empregos-carreira/', views.empregos_carrera, name='empregos_carreira'),
    path('cursos_do_campus/<int:campus_id>/', views.cursos_do_campus, name='cursos_do_campus'),
    path('politica-privacidade/', views.politica_privacidade, name="politica-privacidade"),
   
    
]
