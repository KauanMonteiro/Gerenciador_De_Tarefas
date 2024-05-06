from django.db import models
from usuario.models import Usuario

class Equipe(models.Model):
     nome_equipe = models.CharField( max_length=50)
     membros = models.ManyToManyField(Usuario, related_name='equipes')

     def __str__(self):
          return self.nome_equipe

class Tarefas(models.Model):
     titulo = models.CharField(max_length=100)
     autor = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='tarefas_autor')
     descricao = models.TextField('')
     data_criacao = models.DateTimeField(auto_now_add=True)
     data_limite = models.DateTimeField(auto_now_add=False)
     concluida = models.ManyToManyField(Usuario, blank=True, null=True)
     tarefa_para = models.ForeignKey(Equipe, on_delete=models.CASCADE, null= False)

     def __str__(self):
          return self.titulo
