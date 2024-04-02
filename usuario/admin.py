from usuario.models import Usuario
from django.contrib import admin

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'ativo') 
    search_fields = ('nome', 'email')
    list_filter = ('ativo',)
    list_editable = ('ativo',)