from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Noticia, Categoria
from django.contrib import messages
from django.contrib.messages import constants

@login_required(login_url = '/auth/login')
def home(request):
    noticias = Noticia.objects.filter(autor=request.user)
    return render(request, 'home.html', {'noticias': noticias})

@login_required(login_url='/auth/login')
def escrever_noticia(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        conteudo = request.POST.get('conteudo')
        capa = request.FILES.get('capa')
        categoria = Categoria.objects.get(id=request.POST.get('categoria'))

        noticia = Noticia.objects.create(
            titulo=titulo,
            subtitulo=subtitulo,
            conteudo=conteudo,
            capa=capa,
            categoria=categoria,
            autor=request.user
        )
        
        # Adiciona a mensagem após a criação da notícia
        messages.success(request, 'Notícia criada com sucesso.')
        return redirect('home')  # Redireciona após o sucesso

    categorias = Categoria.objects.all()
    return render(request, 'escrever_noticia.html', {'categorias': categorias})


@login_required(login_url='/auth/login')
def editar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id, autor=request.user)
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        conteudo = request.POST.get('conteudo')
        capa = request.FILES.get('capa')
        categoria_id = request.POST.get('categoria')

        # Validação dos campos
        if titulo and subtitulo and conteudo and categoria_id:
            categoria = get_object_or_404(Categoria, id=categoria_id)

            noticia.titulo = titulo
            noticia.subtitulo = subtitulo
            noticia.conteudo = conteudo
            noticia.categoria = categoria

            # Atualiza a capa somente se um novo arquivo for enviado
            if capa:
                noticia.capa = capa
            
            noticia.save()
            messages.success(request, "Notícia atualizada com sucesso!")
            return redirect('home')  # Você pode redirecionar para a página específica da notícia

        messages.error(request, "Por favor, preencha todos os campos obrigatórios.")
    
    categorias = Categoria.objects.all()
    return render(request, 'editar_noticia.html', {'noticia': noticia, 'categorias': categorias})



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