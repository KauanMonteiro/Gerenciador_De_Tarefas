from django.test import TestCase
from django.urls import reverse,resolve
from tarefas import views

class ViewsTest(TestCase):

    def teste_tarefas_home_view(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func, views.home)
    
    def teste_tarefas_detail_view(self):
        view = resolve(reverse('tarefa_detail',kwargs={'id':1}))
        self.assertIs(view.func, views.tarefa_detail)
    
    def teste_tarefas_concluir_tarefa_view(self):
        view= resolve(reverse('concluir_tarefa', kwargs={'id':1}))
        self.assertIs(view.func,views.concluir_tarefa)
    
    def teste_tarefas_area_usuario_view(self):
        view = resolve(reverse('area_usuario'))
        self.assertIs(view.func, views.area_usuario)

    def teste_tarefas_criar_equipe_view(self):
        view= resolve(reverse('criar_equipe'))
        self.assertIs(view.func, views.criar_equipe)

    def teste_tarefas_equipe_detalhe_view(self):
        view=resolve(reverse('equipe_detalhe', kwargs={'id':1}))
        self.assertIs(view.func,views.equipe_detalhe)

    def teste_tarefa_adicao_usuario_view(self):
        view = resolve(reverse('adicao_usuario',kwargs={'equipe_id':1}))
        self.assertIs(view.func,views.adicao_usuario)

    def teste_tarefas_adicionar_tarefas_view(self):
        view =resolve(reverse('adicionar_tarefas'))
        self.assertIs(view.func,views.adicionar_tarefas)
    
    def teste_tarefas_estatisticas_view(self):
        view = resolve(reverse('estatisticas',kwargs={'equipe_id':1}))
        self.assertIs(view.func,views.estatisticas)

    def teste_tarefas_download_excel_view(self):
        view = resolve(reverse('download_excel', kwargs={'equipe_id':1}))
        self.assertIs(view.func,views.download_excel)




