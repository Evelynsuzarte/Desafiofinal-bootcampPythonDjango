# Nosso squad

- Amparo Silvia Pastor Castillo Runschka
- Andressa Lima Colares
- Evelyn Suzarte Fernandes (líder)
- Helena Sanches Neves de Almeida Rodrigues
- Julia Chaves Silva
- Milena Madeira Muchenski
- Rayane Daryl de Carvalho Pantoja


# Divisão de atividades 

A líder do squad dividiu as atividades para o desafio final de acordo com o que foi discutido em reunião com o squad para a divisão das atividades.
O planejamento da atividade seguiu também a partir da reunião do squad para montar uma modelagem do sistema. As decisões tomadas foram de senso comum a todas as integrantes. Apesar de todas terem suas atividades no desafio, todas tiveram o compromisso de revisar e contribuir com o código.

# Conteúdo complementar
[[Tech Doc] Projeto portal de notícias](https://docs.google.com/document/d/1Rl0bsNkwe33u7iUQSsCE8R_yI662rgQBPCbA6Vj_FXI/edit?usp=sharing)

### Pre sets

- Criar o ambiente virtual: <br>
`python -m venv .venv`

- Ativar o ambiente virtual:  <br>
     - Windows: <br>
`./.venv/scripts/activade`

    -  Linux: <br>
`source venv/bin/activate`

- Após a ativação do ambiente virtual, instalar o requirements: <br>
`pip install -r requirements.txt`


### Códigos úteis para um projeto Django

- Criar um novo app: <br>
`python manage.py startapp nome_app`
    - Após a criação do app é necessário inseri-lo dentro de `setings.py`do projeto principal na lista `INSTALLED_APPS`.

- Criar um novo app: <br>
`python manage.py startapp nome_app`

- Criar um usuário administrador: <br>
`python manage.py createsuperuser`

- Executar alterações no banco de dados: <br>
`python manage.py makemigrations`

- Aplicar alterações no banco de dados: <br>
`python manage.py migrate`
