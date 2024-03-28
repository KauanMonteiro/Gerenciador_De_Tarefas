from django.db import models

class Tarefas(models.Model):
     titulo = models.CharField(max_length=100)
     autor = models.CharField(max_length=50)
     descricao = models.TextField('')
     data_criacao = models.DateTimeField(auto_now_add=True)
     data_limite = models.DateTimeField(auto_now_add=False)
     concluida = models.BooleanField(default=False)

     def __str__(self):
          return self.titulo
