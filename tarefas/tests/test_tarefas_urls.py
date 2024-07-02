from django.test import TestCase
from django.urls import reverse

class UrlsTest(TestCase):
    def teste_tarefas_home_urls(self):
        url = reverse('home')
        self.assertEqual(url, '/')

    def teste_tarefas_tarefa_detail_urls(self):
        url = reverse('tarefa_detail',kwargs={'id':1})
        self.assertEqual(url, '/tarefa/1/')

    def teste_tarefas_concluir_tarefa_urls(self):
        url = reverse('concluir_tarefa', kwargs={'id':1})
        self.assertEqual(url, '/tarefa/1/concluir/')

    def teste_tarefas_area_usuario_urls(self):
        url = reverse('area_usuario')
        self.assertEqual(url, '/area_usuario/')

    def teste_tarefas_criar_equipe_urls(self):
        url = reverse('criar_equipe')
        self.assertEqual(url, '/criar_equipe/')

    def teste_tarefas_equipe_detalhe_urls(self):
        url = reverse('equipe_detalhe',kwargs={'id':1})
        self.assertEqual(url, '/equipe_detalhe/1/')

    def teste_tarefas_adicao_usuario_urls(self):
        url = reverse('adicao_usuario',kwargs={'equipe_id':1})
        self.assertEqual(url, '/adicao_usuario/1/')

    def teste_tarefas_adicionar_tarefas_urls(self):
        url = reverse('adicionar_tarefas')
        self.assertEqual(url, '/adicionar_tarefas/')

    def teste_tarefas_estatisticas_urls(self):
        url = reverse('estatisticas',kwargs={'equipe_id':1})
        self.assertEqual(url, '/estatisticas/1/')

    def teste_tarefas_download_excel_urls(self):
        url = reverse('download_excel', kwargs={'equipe_id':1})
        self.assertEqual(url, '/estatisticas/1/download_excel/')
