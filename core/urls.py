
from django.urls import path
from .views import index, login, cadastrar

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('tela_login.html/', login, name='login'),
    path('tela_login.html/tela_cadastro.html/', cadastrar, name='cadastrar'),
]