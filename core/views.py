from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from empresa.models import CandidatosVaga, Empresa, Vaga

# Create your views here.

def index(request):
    return render(request, 'core/base.html', {})

def home_site(request):
    vagas = Vaga.objects.filter(ativa=True)
    return render(request, 'site/index.html', {'vagas':vagas})

def login_site(request):
    if request.user.is_authenticated:
        try:
            Empresa.objects.get(usuario=request.user)
            return redirect('core:index')
        except:
            return redirect('core:home_site')
        
    if request.method == "POST":
        username = request.POST.get('usuario')
        password = request.POST.get('senha')
        
        usuario = authenticate(request, username=username, password=password)
        
        if usuario:
            login(request, usuario)
            try:
                Empresa.objects.get(usuario=request.user)
                return redirect('core:index')
            except:
                return redirect('core:home_site')
        else:
            return render(request, 'site/login.html', {'erro': 'Usuário ou senha inválidos.'})
        
    return render(request, 'site/login.html', {})

@login_required(login_url='/login')
def logout_site(request):
    logout(request)
    return redirect('core:home_site')

def descricao_vaga(request, slug):
    vagas = Vaga.objects.filter(ativa=True)
    vaga = Vaga.objects.get(slug=slug)
    
    try:
        CandidatosVaga.objects.get(vaga=vaga, candidato__usuario=request.user)
        candidatado = True
    except:
        candidatado = False
    
    data = {
        'vagas': vagas,
        'vaga': vaga,
        'candidatado': candidatado
    }
    return render(request,'site/vaga.html', data)