from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Noticia, Categoria
from django.contrib import messages
from django.contrib.messages import constants


@login_required(login_url = '/auth/login')
def home(request):
    
    return render(request, 'home.html')

def criar_artigo(request):
    return render (request, 'criar_artigo.html')

def criar_artigo(request):
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        conteudo = request.POST.get('conteudo')
        imagem = request.FILES.get('imagem')
        categoria = Categoria.objects.get(id=request.POST.get('categoria'))
        
        noticia = Noticia.objects.create(
            titulo=titulo, subtitulo=subtitulo, conteudo=conteudo, imagem=imagem, categoria=categoria, autor=request.user
        )
        
        return redirect('home')
    
    categorias = Categoria.objects.all()
    return render(request, 'criar_artigo.html', {'categorias': categorias})