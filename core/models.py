from django.db import models




class Usuario(models.Model):
    nome = models.CharField('nome', max_length=100)
    email = models.EmailField('email', unique=True, default='default@example.com')
    senha = models.CharField('senha',max_length=10)
    
    def __str__(self):
        return self.nome

    
    
    

    