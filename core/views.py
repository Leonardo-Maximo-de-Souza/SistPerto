from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'tela_login.html')

def detalhes(request):
    return render(request, 'tela_detalhes.html')

def perfil(request):

    login = request.POST['login']
    senha = request.POST['senha']

    if login == "admin@email.com" and senha == "123@ifrn":
       
        context = {
           "login": login,
            "senha": senha
 
        }   
        return render(request, 'tela_perfil.html',context)
    else:
        return render(request, 'tela_login.html')

def cadastrar(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    contexto = {
        'form': form
    }
    return render(request, 'tela_cadastro.html', contexto)

def itens(request):
    return render(request, 'tela_itens.html')