from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Noticia, Categoria
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Q

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

def buscar_noticias(request):
    query = request.GET.get('q')  # Palavra-chave
    autor = request.GET.get('autor')  # Autor
    categoria = request.GET.get('categoria')  # Categoria

    noticias = Noticia.objects.all()

    # Filtros dinâmicos
    if query:
        noticias = noticias.filter(Q(titulo__icontains=query) | Q(conteudo__icontains=query))

    if autor:
        noticias = noticias.filter(autor__icontains=autor)

    if categoria:
        noticias = noticias.filter(categoria__id=categoria)

    categorias = Categoria.objects.all()  # Para exibir no formulário

    return render(request, 'noticias.html', {
        'noticias': noticias, 
        'query': query, 
        'autor': autor, 
        'categorias': categorias
    })