from django.contrib import admin
from .models import Cliente
from import_export.admin import ExportActionMixin


admin.site.site_header = 'Administração do Cadastro'


class ClienteAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('nome', 'mae', 'email', 'EstadoCivil')


admin.site.register(Cliente, ClienteAdmin) 
