
from django.urls import path
from .views import index, login

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('tela_login.html/', login, name='login'),
]