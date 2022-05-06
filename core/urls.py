from unicodedata import name
from django.urls import path
from core import views

app_name='core'

urlpatterns = [
  path('dashboard', views.index, name='index'),
  path('', views.home_site, name='home_site'),
  path('login', views.login_site, name='login_site'),
  path('logout', views.logout_site, name='logout_site'),
  path('vaga/<str:slug>', views.descricao_vaga, name='descricao_vaga'),
  
]