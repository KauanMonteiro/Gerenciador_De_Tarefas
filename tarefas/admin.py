from django.contrib import admin
from .models import Tarefas, Equipe

@admin.register(Tarefas)
class TarefaAdmin(admin.ModelAdmin):
    pass

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    pass
