from django.shortcuts import render, get_object_or_404
from .models import Tarefas

def home(request):
    tarefas = Tarefas.objects.all()
    return render(request, 'tarefas/pages/home.html', context={'tarefas': tarefas})

def tarefa_detail(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    return render(request, 'tarefas/pages/tarefa_detalhe.html', {'tarefa': tarefa,'is_detail_page': True,
    })
