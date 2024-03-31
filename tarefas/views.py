from django.shortcuts import render, get_object_or_404
from .models import Tarefas

def home(request):
    tarefas_incompletas = Tarefas.objects.filter(concluida=False)
    return render(request, 'tarefas/pages/home.html', {'tarefas': tarefas_incompletas})

def tarefa_detail(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    return render(request, 'tarefas/pages/tarefa_detalhe.html', {'tarefa': tarefa, 'is_detail_page': True})