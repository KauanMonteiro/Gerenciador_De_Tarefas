from django.shortcuts import render, get_object_or_404 , redirect
from django.urls import reverse 
from .models import Tarefas, Equipe
from usuario.models import Usuario

def home(request):
    if 'usuario' not in request.session:
        return redirect('login')

    usuario_id = request.session['usuario']
    usuario = Usuario.objects.get(pk=usuario_id)
    
    if usuario.equipes.exists():
        equipe_usuario = usuario.equipes.first()
        tarefas_incompletas = Tarefas.objects.filter(concluida=False, tarefa_para=equipe_usuario)
        return render(request, 'tarefas/pages/home.html', {'tarefas': tarefas_incompletas, 'usuario': usuario})
    else:
        return render(request, 'tarefas/pages/home.html')

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
    
    usuario_id = request.session['usuario']
    usuario = Usuario.objects.get(pk=usuario_id)
    
    if usuario.equipes.exists():
        equipes_usuario = usuario.equipes.all()
        tarefas_equipes_usuario = Tarefas.objects.filter(tarefa_para__in=equipes_usuario)
        
        tarefas_nao_concluidas = tarefas_equipes_usuario.filter(concluida=False).count()
        total_tarefas = tarefas_equipes_usuario.count()
        tarefas_concluidas = tarefas_equipes_usuario.filter(concluida=True).count()
        
        return render(request, 'tarefas/pages/area_usuario.html', {
            'usuario': usuario,
            'tarefas': tarefas_equipes_usuario,
            'equipes': equipes_usuario,
            'tarefas_nao_concluidas': tarefas_nao_concluidas,
            'total_tarefas': total_tarefas,
            'tarefas_concluidas': tarefas_concluidas
        })
    else:
        return render(request, 'tarefas/pages/home.html')

def criar_equipe(request):
    if 'usuario' not in request.session:
        return redirect('login')
    
    usuario_id = request.session['usuario']
    usuario = Usuario.objects.get(pk=usuario_id)
    
    if usuario.cargo != 'Professor':
        return render(request, 'tarefas/pages/home.html')
    else:
        if request.method == 'POST':
            nome = request.POST.get('nome')

            if len(nome.strip()) == 0:
                return render(request, 'tarefas/pages/criar_equipe.html')
            
            else:
                equipe = Equipe(nome_equipe=nome)
                equipe.save()
                return redirect(reverse('home'))
        
        return render(request, 'tarefas/pages/criar_equipe.html')