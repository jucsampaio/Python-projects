from rest_framework import viewsets, generics
from book_data.models import Livro, Autor
from book_data.serializer import LivroSerializer, AutorSerializer,ListaLivroAutorSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AutoresViewSet(viewsets.ModelViewSet):
    """Exibindo autores"""
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]


class LivrosViewSet(viewsets.ModelViewSet):
    """Exibindo todos livros"""
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class ListaLivrosAutor(generics.ListAPIView):
    """Listas dos Livros de um Autor"""
    def get_queryset(self):
        queryset=Livro.objects.filter(autor_id=self.kwargs['pk'])
        return queryset
    serializer_class= ListaLivroAutorSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
        
        
        
        
        
    

    