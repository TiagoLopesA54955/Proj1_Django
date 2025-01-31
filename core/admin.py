from django.contrib import admin

from .models import Produto, Cliente
# Register your models here.
# adicionar modelos para a visao admin
 
# classe para mudar o display da lista de produtos 
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'estoque']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'apelido', 'email']

admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Cliente,ClienteAdmin)

