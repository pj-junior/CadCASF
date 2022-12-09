from datetime import datetime
from urllib import request

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Cliente
from .forms import ClienteForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


def home(request):
    clientes = Cliente.pk
    contexto = {
        clientes: clientes,
         
    }
    resposta = render(request, template_name="clientes/home.html", context=contexto)

    return HttpResponse(resposta)


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/cliente_form.html"
    success_url = reverse_lazy('home')
    success_message = "Exemplo deletado com sucesso!!"

  
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/cliente_form.html"
    success_url = reverse_lazy('home')
    


def detalhes_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    contexto = {
       'cliente': cliente,    
    }
    
    resposta = render(request, template_name="clientes/cliente.html", context=contexto)
    return HttpResponse(resposta)
   
    
def deleta_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('home') 
