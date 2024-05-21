from django.db import models
from usuario.models import Usuario

class Equipe(models.Model):
     nome_equipe = models.CharField( max_length=50)
     membros = models.ManyToManyField(Usuario, related_name='equipes')

     def __str__(self):
          return self.nome_equipe

class Tarefas(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tarefas_autor')
    descricao = models.TextField(null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_limite = models.DateTimeField(null=True)
    concluida = models.ManyToManyField(Usuario, blank=True)
    tarefa_para = models.ManyToManyField(Equipe)
    alternativa1 = models.TextField(null=True,blank=True)
    alternativa2 = models.TextField(null=True,blank=True)
    alternativa3 = models.TextField(null=True,blank=True)
    alternativa4 = models.TextField(null=True,blank=True)
    alternativa5 = models.TextField(null=True,blank=True)
    alternativa_correta = models.IntegerField(choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')], null=True)
    
    def __str__(self):
        return self.titulo
