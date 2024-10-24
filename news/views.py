from django.shortcuts import render, get_object_or_404
from plataforma.models import Noticia

def news_feed(request):
    noticias = Noticia.objects.filter(status='PU')
    return render(request, 'news_feed.html', {'noticias': noticias})

def news_completa(request, id):
    noticia = get_object_or_404(Noticia, id=id)  
    return render(request, 'news_completa.html', {'noticia': noticia})