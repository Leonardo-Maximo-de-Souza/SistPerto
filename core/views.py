from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        try:
            usuario = Usuario.objects.get(email=email, senha=senha)
            context = {
                "usuario": usuario
            }
            return render(request, 'tela_perfil.html', context)
        except Usuario.DoesNotExist:
            return render(request, 'tela_login.html', {'error': 'Login inválido'})
    return render(request, 'tela_login.html')

def detalhes(request):
    return render(request, 'tela_detalhes.html')

def perfil(request):
    return render(request, 'tela_perfil.html')

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
