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
        tarefas_incompletas = Tarefas.objects.exclude(concluida=usuario, tarefa_para=equipe_usuario)
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

    usuario_id = request.session['usuario']
    usuario = Usuario.objects.get(pk=usuario_id)

    tarefa = get_object_or_404(Tarefas, pk=id)

    if usuario in tarefa.tarefa_para.membros.all():
        if not tarefa.concluida.filter(pk=usuario_id).exists():
            tarefa.concluida.add(usuario)
    return redirect(reverse('home'))

def area_usuario(request):
    if 'usuario' not in request.session:
        return redirect('login')
    
    usuario_id = request.session['usuario']
    usuario = Usuario.objects.get(pk=usuario_id)
    
    if usuario.equipes.exists():
        equipes_usuario = usuario.equipes.all()
        tarefas_equipes_usuario = Tarefas.objects.filter(tarefa_para__in=equipes_usuario)
        
        tarefas_nao_concluidas = tarefas_equipes_usuario.exclude(concluida= usuario).count()
        total_tarefas = tarefas_equipes_usuario.count()
        tarefas_concluidas = tarefas_equipes_usuario.filter(concluida=usuario ).count()
        return render(request, 'tarefas/pages/area_usuario.html', {
            'usuario': usuario,
            'tarefas': tarefas_equipes_usuario,
            'equipes': equipes_usuario,
            'tarefas_nao_concluidas': tarefas_nao_concluidas,
            'total_tarefas': total_tarefas,
            'tarefas_concluidas': tarefas_concluidas,
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

def equipe_detalhe(request, id):
    if 'usuario' not in request.session:
        return redirect('login')
    
    usuario_id = request.session['usuario']
    usuario = Usuario.objects.get(pk=usuario_id)
    
    equipe = get_object_or_404(Equipe, pk=id)
    tarefas_equipe = Tarefas.objects.filter(tarefa_para=equipe)
    
    return render(request, 'tarefas/pages/ver_mais_equipe.html', {'equipe': equipe, 'tarefas': tarefas_equipe, 'usuario': usuario})
    

def adicao_usuario(request, equipe_id):
    if 'usuario' not in request.session:
        return redirect('login')
    
    if request.method == 'POST':
        userId = request.POST.get('userId')

        if len(userId.strip()) == 0:
            return redirect('adicao_usuario', equipe_id=equipe_id)
        
        else:
            try:
                equipe = Equipe.objects.get(id=equipe_id)
                usuario = Usuario.objects.get(id=userId)
                equipe.membros.add(usuario)
                equipe.save()
                return redirect('area_usuario')
            except Equipe.DoesNotExist:
                pass

    return render(request, 'tarefas/pages/adicionar_usuario.html',{'equipe_id': equipe_id})

def adicionar_tarefas(request):
    if 'usuario' not in request.session:
        return redirect('login')
    
    usuario_id = request.session['usuario']
    usuario = Usuario.objects.get(pk=usuario_id)
    equipe = usuario.equipes.all()
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_limite = request.POST.get('data_limite')
        tarefa_para = request.POST.getlist('tarefa_para')

        if not (titulo and descricao and tarefa_para):
            return redirect('adicionar_tarefas')
        else:
            tarefa = Tarefas.objects.create(titulo=titulo, descricao=descricao, data_limite=data_limite, autor=usuario)
            tarefa.tarefa_para.set(tarefa_para)
            tarefa.save()
            return redirect('home')
    return render(request, 'tarefas/pages/adicionar_tarefa.html', {'equipes': equipe})
