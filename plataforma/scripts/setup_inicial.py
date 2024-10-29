from django.contrib.auth import get_user_model
from plataforma.models import Categoria  

# def criar_superusuario():
#     User = get_user_model()
#     if not User.objects.filter(is_superuser=True).exists():
#         User.objects.create_superuser(
#             username="admin",        
#             email="admin@example.com", 
#             password="admin1234"     
#         )
#         print("Superusuário criado com sucesso!")
#     else:
#         print("Superusuário já existe.")

def inserir_dados():
    print("Verificando se as categorias existem...")
    dados = [
        {"nome": "Empregabilidade"},
        {"nome": "Força feminina"},
        {"nome": "Programação"},
        {"nome": "Educação"},
        {"nome": "Empreendedorismo"},
    ]
    
    for dado in dados:
        # Verifica se a categoria já existe
        if not Categoria.objects.filter(nome=dado["nome"]).exists():
            instancia = Categoria(**dado)
            instancia.save()
            print(f"Categoria '{dado['nome']}' inserida com sucesso!")
        else:
            print(f"A categoria '{dado['nome']}' já existe.")


def setup_inicial():
    # criar_superusuario()
    inserir_dados()
