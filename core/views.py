from django.shortcuts import render

# Lista de serviços
servicos = [
    {"nome": "Desenvolvimento Web", "descricao": "Criação de sites e apps", "preco": 2500.00},
    {"nome": "Consultoria", "descricao": "Análise de sistemas", "preco": 1800.00},
    {"nome": "Suporte Técnico", "descricao": "Suporte remoto e presencial", "preco": 500.00},
]

# Lista de cursos
cursos = [
    {"nome": "Python Básico", "descricao": "Introdução à programação com Python", "carga_horaria": 40, "preco": 800.00},
    {"nome": "Django Completo", "descricao": "Desenvolvimento web com Django", "carga_horaria": 60, "preco": 1200.00},
    {"nome": "Banco de Dados", "descricao": "Gestão de dados com SQL", "carga_horaria": 50, "preco": 1000.00},
]

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def servicos(request):
    return render(request, 'servicos.html')

def cursos(request):
    return render(request, 'cursos.html')

