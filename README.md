# Blog em Django – Curso Python Coderhouse

Este projeto foi desenvolvido como parte do curso de Python da Coderhouse.

O site foi criado utilizando Django, com o padrão de arquitetura MTV (Model-Template-View). A proposta principal foi criar uma aplicação web com herança de templates, formulários e uma funcionalidade de busca.

## Funcionalidades

- Cadastro de autores
- Cadastro de posts
- Cadastro de comentários
- Busca de posts pelo título

## Como executar o projeto

1. Clone o repositório
2. Crie um ambiente virtual
3. Instale as dependências com `pip install -r requirements.txt`
4. Rode as migrações com `python manage.py migrate`
5. Inicie o servidor com `python manage.py runserver`

## Rotas principais

- `/autor/` → Cadastro de autores
- `/post/` → Cadastro de posts
- `/comentario/` → Cadastro de comentários
- `/buscar/` → Busca por título de post
