from django.conf import settings
from django.db import models

# Create your models here.

class Candidato(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=500)
    foto = models.ImageField(blank=True, null=True)
    cpf = models.CharField('CPF', max_length=50, unique=True)
    email = models.EmailField('Email')
    telefone = models.CharField('Telefone', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    
    def __str__(self):
        return self.nome