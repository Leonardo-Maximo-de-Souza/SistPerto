from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'tela_login.html')

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
    return render(request, 'tela_cadastro.html')

def itens(request):
    return render(request, 'tela_itens.html')