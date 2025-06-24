# 📋 Projeto: Django Todo List

Este é um projeto simples de lista de tarefas (Todo List) desenvolvido em **Python com Django**. Nele é possível **adicionar**, **editar**, **marcar como concluída** e **excluir** tarefas. O front-end usa o **Bootstrap 5** para estilização.

---

## 🚀 Como executar o projeto localmente

### ✅ Pré-requisitos:

- Python 3.x instalado
- Pip instalado
- Virtualenv (opcional, mas recomendado)

---

### 🔧 Passo a passo:

1. **Clone o repositório**
2. Ative o ambiente:
- Windows:
```venv\Scripts\activate```
- Linux / Mac:
```source venv/bin/activate```
3. Instale as dependências:
```pip install django```
4. Execute as migrações:
```
python manage.py makemigrations
python manage.py migrate
```
5.	(Opcional) Crie um superusuário para acessar o painel admin
```
python manage.py createsuperuser
```
- depois de ter criado o usuario e a senha acesse o endereço:
http://127.0.0.1:8000/admin/
6. Rode o servidor local:
- Windows:
```
python manage.py runserver
```
- Linux / Mac:
```
python3 manage.py runserver
```
7. Depois, abra o navegador e acesse:

http://127.0.0.1:8000/
<br>
Para parar de rodar so aperte: Control + C

---

## ⚙️ Estrutura básica do Django usada:

- Models: Para criar a estrutura da Tarefa no banco de dados
- Views: Para tratar as requisições (GET, POST)
- Templates: HTML com Bootstrap para o front-end
- Admin: Visualização e gerenciamento de tarefas via Django Admin
- Banco de Dados: SQLite (padrão do Django)

## 🌍 Configurações Regionais:
- Time Zone: America/Sao_Paulo

### 📌 Observações finais:

Este projeto foi desenvolvido com foco em aprendizado prático de Django básico, CRUD, Bootstrap e integração com banco de dados.

Sinta-se à vontade para testar, sugerir melhorias ou adaptar!

## 👩🏻‍💻 Autor:
- Nome: Késia
- Curso: Engenharia de Software, Disciplina: Novas Tecnologias, Professor: Victor Zerefos
- Instituição: Universidade Cátolica de Brasília - UCB








