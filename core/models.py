from django.db import models

# Create your models here.
# Criar os modelos de dados (classes) da BD

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Quantidade em Estoque')
    
    # metodo para retornar o nome do produto na lista de produtos
    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    apelido = models.CharField('Apelido', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    
    def __str__(self):
        return self.nome + ' ' + self.apelido