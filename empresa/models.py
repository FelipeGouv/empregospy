from tkinter import CASCADE
from django.db import models
from django.conf import settings
from slugify import slugify
from datetime import datetime
from random import randint
from candidato.models import Candidato
# Create your models here.

class Empresa(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=1024)
    cpnj = models.CharField('CNPJ', max_length=100, unique=True)
    logo = models.ImageField('Logo', null=True, blank=True)
    
    def __str__(self):
        return self.nome
    
class Vaga(models.Model):
    slug = models.SlugField('slug', unique=True, null=True, blank=True, max_length=1000)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    cargo = models.CharField('Cargo', max_length=1000)
    salario = models.FloatField('Salário')
    descricao = models.TextField('Descrição')
    candidatos = models.IntegerField('Candidatos', default=0)
    criada_em = models.DateField('Criado Em', auto_now_add=True)
    beneficios = models.CharField('Benefícios', max_length=1000)
    qtd_vagas = models.IntegerField('Quantidade de Vagas', default=1)
    ativa = models.BooleanField('Ativa', default=True)
    cidade = models.CharField('Cidade', max_length=1024)
    
    def __str__(self):
        return self.empresa.nome +' '+ self.cargo
    
    def save(self, *args, **kwargs):
        created = False
        while(not created):
            try:
                numero = randint(0,10000)
                self.slug = slugify(f'{numero} - {self.cargo}')
                Vaga.objects.get(slug=self.slug)
            except:
                created = True
        super().save(*args, **kwargs)
    
    def qtd_candidatos(self):
        return CandidatosVaga.objects.filter(vaga=self).count()
            
class CandidatosVaga(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    data_cadastro = models.DateField('Data Cadatro', auto_now_add=True)
    aprovado = models.BooleanField('Aprovado', default=False)
    
