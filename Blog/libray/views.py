from django.shortcuts import render

def index(request):
        return render(request, 'galeria/index.html')

def about(request):
        return render(request, 'galeria/about.html')

def contact(request):
        return render(request, 'galeria/contact.html')

def post(request):
        return render(request, 'galeria/post.html')

def morteintern(request):
        return render(request, 'resenhas/morteintern.html')






