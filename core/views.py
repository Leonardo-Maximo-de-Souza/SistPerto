from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'tela_login.html')

def cadastrar(request):
    return render(request, 'tela_cadastro.html')