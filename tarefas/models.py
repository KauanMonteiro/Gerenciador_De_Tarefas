from django.db import models
from usuario.models import Usuario

class Equipe(models.Model):
     nome_equipe = models.CharField( max_length=50)
     membros = models.ManyToManyField(Usuario, related_name='equipes')

     def __str__(self):
          return self.nome_equipe

class Tarefas(models.Model):
     titulo = models.CharField(max_length=100)
     autor = models.CharField(max_length=50)
     descricao = models.TextField('')
     data_criacao = models.DateTimeField(auto_now_add=True)
     data_limite = models.DateTimeField(auto_now_add=False)
     concluida = models.BooleanField(default=False)
     tarefa_para = models.ForeignKey(Usuario, on_delete=models.CASCADE, null= False)

     def __str__(self):
          return self.titulo
