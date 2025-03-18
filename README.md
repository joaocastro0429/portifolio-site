# Documentação do Projeto: Portfólio

## 1. Visão Geral

Este é um projeto de portfólio desenvolvido com Django e estilizado com Bootstrap. O objetivo do projeto é criar um site pessoal para exibir os meus projetos, 
habilidades e informações de contato de forma organizada e atraente.

### Tecnologias Utilizadas
- **Django**: Framework de desenvolvimento web em Python.
- **Bootstrap**: Framework front-end para estilização responsiva.
- **Python**: Linguagem de programação utilizada para o back-end.
- **HTML/CSS**: Para estruturação e estilo da página.

## 2. Funcionalidades

O portfólio possui as seguintes funcionalidades:
- Exibição de informações pessoais.
- Lista de projetos com descrições detalhadas.
- Página de contato com formulário para enviar mensagens.
- Interface responsiva, adaptando-se para diferentes dispositivos (celular, tablet, desktop).

## 3. Estrutura do Projeto

### Diretórios principais:
- `myportfolio/`: Pasta principal do projeto.
    - `myportfolio/settings.py`: Configurações do projeto Django.
    - `myportfolio/urls.py`: Definição das rotas do projeto.
    - `myportfolio/wsgi.py`: Arquivo de inicialização do servidor.
    - `portfolio/`: Aplicação Django responsável pela lógica do portfólio.
        - `views.py`: Define as views (funções que retornam as respostas das páginas).
        - `urls.py`: Definição das URLs relacionadas à aplicação de portfólio.
        - `templates/`: Contém os templates HTML.
            - `portifolio.html`: Arquivo base com a estrutura comum (cabeçalho, rodapé, etc).
            - `static/`: Arquivos estáticos como CSS e JS.
            - `css/`: Arquivos de estilo.
            - `js/`: Arquivos de script JavaScript.

## 4. Instalação

Para rodar o projeto localmente, siga os passos abaixo:

1. **Clone o repositório do projeto**:
    ```bash
    git clone https://github.com/usuario/portfolio.git
    cd portfolio
    ```

2. **Crie um ambiente virtual**:
    ```bash
    python -m venv venv
    ```

3. **Ative o ambiente virtual**:
    - No Windows:
      ```bash
      venv\Scripts\activate
      ```
    - No macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Inicie o servidor de desenvolvimento**:
    ```bash
    python manage.py runserver
    ```

6. **Acesse o projeto**: Abra o navegador e vá para `http://127.0.0.1:8000/`.

## 5. Personalização

Você pode personalizar o layout e as funcionalidades do seu portfólio de acordo com suas necessidades.

### Modificando o tema
- O layout do portfólio utiliza o framework **Bootstrap**. Você pode alterar os componentes de estilo e as classes para personalizar o visual, como as cores, fontes e a disposição dos elementos.

### Adicionando novos projetos
- Como não estamos utilizando um banco de dados, você pode adicionar os projetos diretamente no código, dentro dos arquivos de template ou até mesmo criando um arquivo JSON ou YAML para armazenar os dados dos projetos e carregá-los nas páginas. Isso pode ser feito manipulando dados diretamente nas views ou nas variáveis passadas para os templates.

## 6. Considerações Finais

Este portfólio serve como um exemplo simples de como construir um site pessoal utilizando Django e Bootstrap sem a necessidade de um banco de dados. Você pode expandir o projeto incluindo mais funcionalidades, como um blog, integração com redes sociais, ou até mesmo uma área de login para os visitantes.
