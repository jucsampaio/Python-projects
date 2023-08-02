from rest_framework import serializers
from book_data.models import Livro, Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome', 'descricao', 'genero' ]
        
class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        exclude=[]
       

class ListaLivroAutorSerializer(serializers.ModelSerializer):
   class Meta:
        model = Livro
        fields = ['nome', 'publicacao_ano']
