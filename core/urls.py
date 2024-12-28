
from django.urls import path
from .views import index, login, cadastrar, perfil, itens

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('tela_login.html/', login, name='login'),
    path('tela_perfil.html/', perfil, name='perfil'),
    path('tela_login.html/tela_cadastro.html/', cadastrar, name='cadastrar'),
    path('tela_itens.html/', itens, name='itens'),
]