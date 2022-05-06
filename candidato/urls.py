from django.urls import path
from candidato import views

app_name='candidato'

urlpatterns = [
  path('candidatar/<str:slug>', views.candidatar, name='candidatar'),
  path('deixarvaga/<str:slug>', views.deixarvaga, name='deixarvaga'),
  
]