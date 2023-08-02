from django.contrib import admin
from django.urls import path, include 
from book_data.views import LivrosViewSet, AutoresViewSet,ListaLivrosAutor
from rest_framework import routers

router = routers.DefaultRouter()
router.register('livros',LivrosViewSet, basename='livros')
router.register('autores', AutoresViewSet, basename='autores')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('autor/<int:pk>/livros/', ListaLivrosAutor.as_view())
]