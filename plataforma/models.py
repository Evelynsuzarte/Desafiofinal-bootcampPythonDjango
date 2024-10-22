from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.TextField()
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='noticias')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)   

    def __str__(self):
        return self.titulo
    
    