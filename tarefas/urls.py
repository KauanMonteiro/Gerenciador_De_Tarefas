from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tarefa/<int:id>/', views.tarefa_detail, name='tarefa_detail'),
    path('tarefa/<int:id>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
    path('area_usuario/', views.area_usuario, name='area_usuario'),
    path('criar_equipe/', views.criar_equipe, name= 'criar_equipe'),
    path('equipe_detalhe/<int:id>/', views.equipe_detalhe, name='equipe_detalhe'),
    path('adicao_usuario/<int:equipe_id>/', views.adicao_usuario, name='adicao_usuario'),
    path('adicionar_tarefas/', views.adicionar_tarefas, name='adicionar_tarefas'),
    ]

