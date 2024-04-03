from django.shortcuts import render, get_object_or_404 , redirect
from django.urls import reverse 
from .models import Tarefas

def home(request):
    if 'usuario' not in request.session:
        return redirect('login')
    tarefas_incompletas = Tarefas.objects.filter(concluida=False)
    return render(request, 'tarefas/pages/home.html', {'tarefas': tarefas_incompletas})

def tarefa_detail(request, id):
    if 'usuario' not in request.session:
        return redirect('login')
    tarefa = get_object_or_404(Tarefas, pk=id)
    return render(request, 'tarefas/pages/tarefa_detalhe.html', {'tarefa': tarefa, 'is_detail_page': True})

def concluir_tarefa(request, id):
    if 'usuario' not in request.session:
        return redirect('login')
    tarefa = get_object_or_404(Tarefas, pk=id)
    if not tarefa.concluida:
        tarefa.concluida = True
        tarefa.save()
    return redirect(reverse('home'))


def area_usuario(request):
    if 'usuario' not in request.session:
        return redirect('login')
    tarefas = Tarefas.objects.all()
    return render(request, 'tarefas/pages/area_usuario.html', {'tarefas': tarefas})
