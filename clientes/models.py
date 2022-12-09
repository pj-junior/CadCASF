from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    mae = models.CharField(max_length=100, verbose_name='Mãe')
    email = models.EmailField(verbose_name='E-Mail')
    estcivil_choice = (
       ('Solteiro', 'Solteiro'),
       ('Casado', 'Casado'),
       ('Separado', 'Separado'),
       ('Divorciado', 'Divorciado'),
       ('Viúvo', 'Viúvo'))   
    EstadoCivil = models.CharField(max_length=20, blank=True, null=True, choices=estcivil_choice, verbose_name='Estado Civil')   
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    rg = models.CharField(max_length=20, verbose_name='RG')
    telefone = models.CharField(max_length=17, verbose_name='Telefone')
    celular = models.CharField(max_length=17, verbose_name='Celular')
    endereco = models.CharField(max_length=100, verbose_name='Endereço')
    nnum = models.IntegerField(verbose_name='Número')
    complemento = models.CharField(max_length=100, verbose_name='Complemento')
    bairro = models.CharField(max_length=50, verbose_name='Bairro')
    cidade = models.CharField(max_length=50, verbose_name='Cidade')  
    uf_choice = (
      ('AC', 'Acre'),
      ('AL', 'Alagoas'),
      ('AP', 'Amapá'),
      ('AM', 'Amazonas'),
      ('BA', 'Bahia'),
      ('CE', 'Ceará'),
      ('DF', 'Distrito Federal'),
      ('ES', 'Espírito Santo'),
      ('GO', 'Goiás'),
      ('MA', 'Maranhão'),
      ('MG', 'Minas Gerais'),
      ('MS', 'Mato Grosso do Sul'),
      ('MT', 'Mato Grosso'),
      ('PA', 'Pará'),
      ('PB', 'Paraíba'),
      ('PE', 'Pernanbuco'),
      ('PI', 'Piauí'),
      ('PR', 'Paraná'),
      ('RJ', 'Rio de Janeiro'),
      ('RN', 'Rio Grande do Norte'),
      ('RO', 'Rondônia'),
      ('RR', 'Roraima'),
      ('RS', 'Rio Grande do Sul'),
      ('SC', 'Santa Catarina'),
      ('SE', 'Sergipe'),
      ('SP', 'São Paulo'),
      ('TO', 'Tocantins')
    )  
    uf = models.CharField(max_length=20, blank=True, null=True, choices=uf_choice, verbose_name='UF')
    cep = models.CharField(max_length=10, verbose_name='CEP')


class Meta:
    db_table = 'cliente'
    verbose_name = 'Cliente'
    verbose_name_plural = 'Clientes'


def __unicode__(self):
    return self.nome


def __str__(self):
    return self.nome


