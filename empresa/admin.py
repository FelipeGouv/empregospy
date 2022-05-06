from django.contrib import admin
from empresa.models import Empresa, Vaga, CandidatosVaga
# Register your models here.

admin.site.register(Empresa)
admin.site.register(Vaga)
admin.site.register(CandidatosVaga)
