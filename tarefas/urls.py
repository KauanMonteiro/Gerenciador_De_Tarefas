from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tarefa/<int:id>/', views.tarefa_detail, name='tarefa_detail'),
    path('tarefa/<int:id>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    path('area_usuario/', views.area_usuario, name='area_usuario'),
    path('criar_equipe/', views.criar_equipe, name= 'criar_equipe'),
    ]

