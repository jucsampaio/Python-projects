from django.contrib import admin
from book_data.models import Livro, Autor

class Autores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

admin.site.register(Autor, Autores)
    
class Livros(admin.ModelAdmin):
    #campus para aparecer no admin
    list_display = ('id', 'nome', 'autor','editora', 'publicacao_ano')
    
    #alterar algum livro
    list_display_links = ('id', 'nome')
    
    #buscar algum livro
    search_fields = ('nome',) 
    
    # mostar a quantidade de livros por pagina
    list_per_page = 20
    
admin.site.register(Livro, Livros)




