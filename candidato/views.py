from django.http import JsonResponse
from django.shortcuts import redirect, render
from candidato.models import Candidato
from empresa.models import CandidatosVaga, Vaga
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def candidatar(request, slug):
    candidato = Candidato.objects.get(usuario=request.user)
    vaga = Vaga.objects.get(slug=slug)
    
    CandidatosVaga.objects.get_or_create(candidato=candidato, vaga=vaga)
    
    return redirect(f'/vaga/{slug}')

def deixarvaga(request, slug):
    candidato = Candidato.objects.get(usuario=request.user)
    vaga = Vaga.objects.get(slug=slug)
    
    CandidatosVaga.objects.filter(candidato=candidato, vaga=vaga).delete()
    
    return redirect(f'/vaga/{slug}')