from django import forms
from clientes.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
          #[
          #"nome", 
          #'mae', 
          #'endereco', 
          #'complemento', 
          #'bairro', 
          #'cidade', 
          #'cep', 
          #'telefone', 
          #'celular', 
          #'cpf', 
          #'rg', 
          #'email'
  #  ]
      
