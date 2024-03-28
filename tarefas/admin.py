from django.contrib import admin
from .models import Tarefas

@admin.register(Tarefas)
class TarefasAdmin(admin.ModelAdmin):
    pass