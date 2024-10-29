from django.shortcuts import render, get_object_or_404
from plataforma.models import Noticia, Categoria
from django.db.models import Q


def news_feed(request):
    noticias = Noticia.objects.filter(status='PU')
    categorias = Categoria.objects.all()
    return render(request, 'news_feed.html', {'noticias': noticias, 'categorias': categorias})

def news_completa(request, id):
    noticia = get_object_or_404(Noticia, id=id)  
    return render(request, 'news_completa.html', {'noticia': noticia})

def buscar_noticias(request):
    query = request.GET.get('q')
    autor = request.GET.get('autor')
    categoria = request.GET.get('categoria')

    noticias = Noticia.objects.filter(status='PU')

    if query:
        noticias = noticias.filter(Q(titulo__icontains=query) | Q(conteudo__icontains=query))

    if autor:
        noticias = noticias.filter(autor__username__icontains=autor)  

    if categoria:
        noticias = noticias.filter(categoria__id=int(categoria)) 
        
    if not autor and not query and not categoria:
        pass

    categorias = Categoria.objects.all()

    return render(request, 'resultado_busca.html', {
        'noticias': noticias,
        'query': query,
        'autor': autor,
        'categoria': categoria,  
        'categorias': categorias
    })