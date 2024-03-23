from django.shortcuts import render
from django.http import request

def home(request):
    return render(request,'tarefas/pages/home.html')