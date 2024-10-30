# plataforma/management/commands/inserir_dados.py
from django.core.management.base import BaseCommand
from plataforma.models import Categoria

class Command(BaseCommand):
    help = 'Insere categorias iniciais no banco de dados'

    def handle(self, *args, **kwargs):
        print("Verificando se as categorias existem...")
        dados = [
            {"nome": "Empregabilidade"},
            {"nome": "Força feminina"},
            {"nome": "Programação"},
            {"nome": "Educação"},
            {"nome": "Empreendedorismo"},
            {"nome": "Pesquisa"},
        ]
        
        for dado in dados:
            if not Categoria.objects.filter(nome=dado["nome"]).exists():
                instancia = Categoria(**dado)
                instancia.save()
                print(f"Categoria '{dado['nome']}' inserida com sucesso!")
            else:
                print(f"A categoria '{dado['nome']}' já existe.")
        self.stdout.write(self.style.SUCCESS("Inserção de dados concluída com sucesso."))
