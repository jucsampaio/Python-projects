from django.db import models

class Autor(models.Model):
    GENERO = (
        ('D', 'Drama'),
        ('S', 'Suspense'),
        ('R', 'Romance'),
        ('F', 'Fantasia'),
        ('B', 'Biografia')
    )
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    genero = models.CharField(max_length=1, choices=GENERO, blank= False, null=False, default='R')
    
    def __str__ (self):
        return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    editora = models.CharField(max_length=100) 
    publicacao_ano = models.DateField()
    autor = models.ForeignKey(Autor, null=True, on_delete=models.CASCADE)
    
    #representar cada livro pelo nome
    def __str__ (self):
        return self.nome
    
