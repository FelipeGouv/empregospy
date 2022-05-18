from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from candidato.models import Candidato
from core.forms import CandidatoForm
from empresa.models import CandidatosVaga, Empresa, Vaga

# Create your views here.

def index(request):
    return render(request, 'core/base.html', {})

def home_site(request):
    vagas = Vaga.objects.filter(ativa=True)
    return render(request, 'site/index.html', {'vagas':vagas})

def login_site(request):
    redirect_url = 'core:home_site'
    if request.GET.get('next'):
        redirect_url = request.GET.get('next')
    if request.user.is_authenticated:
        try:
            Empresa.objects.get(usuario=request.user)
            return redirect('core:index')
        except:
            return redirect(redirect_url)
        
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
                return redirect(redirect_url)
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

def empresas(request):
    empresas = Empresa.objects.all()
    
    for empresa in empresas:
        empresa.vagas = Vaga.objects.filter(empresa=empresa, ativa=True)[0:4]
    
    return render(request, 'site/empresas.html', {'empresas':empresas})

def meu_cadastro(request):
    candidato = Candidato.objects.get(usuario=request.user)
    
    return render(request , 'site/meu_cadastro.html', {'candidato':candidato})

def editar_cadastro(request):
    candidato = Candidato.objects.get(usuario=request.user)
    if request.method == 'POST':
        form = CandidatoForm(request.POST, request.FILES, instance=candidato)
    
        if form.is_valid():
            form.save()
            return redirect('core:meu_cadastro')
    else:
        form = CandidatoForm(instance=candidato)
    
    print(form.errors)
    return render(request, 'site/editar_cadastro.html', {'form':form})
    