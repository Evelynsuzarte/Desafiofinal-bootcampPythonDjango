from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Noticia, Categoria
from django.contrib import messages
from django.contrib.messages import constants

@login_required(login_url = '/auth/login')
def home(request):
    noticias = Noticia.objects.filter(autor=request.user)
    return render(request, 'home.html', {'noticias': noticias})

@login_required(login_url = '/auth/login')
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

def excluir_noticia(request, id):
    if request.method == 'POST':
        noticia = get_object_or_404(Noticia, id=id)
        noticia.delete()
        messages.add_message(request, constants.SUCCESS, "Notícia excluída com sucesso.")
        return redirect('home')
    else:
        messages.add_message(request, constants.ERROR, "Você não tem permissão para excluir uma notícia.")
        return redirect('home')


    
def news_completa(request, id):
    noticia = get_object_or_404(Noticia, id=id)  
    return render(request, 'news_completa.html', {'noticia': noticia})