from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('home/criar_artigo/', views.criar_artigo, name='criar_artigo'),
    path('excluir_noticia/<int:id>/', views.excluir_noticia, name='excluir_noticia'),
    path('editar_noticia/<int:id>/', views.editar_noticia, name='editar_noticia'),
    path('news_completa/<int:id>/', views.news_completa, name='news_completa'), 

]