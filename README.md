# Sistema de Cadastro de Alunos - COMPET Médio SophIA

Este repositório contém o trabalho de conclusão do Módulo 2 - Streamlit do projeto COMPET Médio SophIA, desenvolvido na Escola Técnica Estadual Porto Digital. O sistema é uma aplicação web interativa para cadastro e gerenciamento de alunos, construída utilizando a biblioteca Streamlit do Python.

## Sobre o Projeto

O projeto COMPET Médio SophIA visa capacitar estudantes em tecnologias emergentes. Este módulo, focado em Streamlit, permitiu a criação de uma ferramenta prática para a gestão de dados de alunos, incluindo funcionalidades de login, cadastro, listagem, edição e exclusão de registros, além de um dashboard interativo para visualização de dados.

## Autor

Eduardo Lira dos Santos

## Funcionalidades

O sistema oferece as seguintes funcionalidades principais:

*   **Sistema de Login e Cadastro de Usuários:** Autenticação de usuários para acesso seguro ao sistema.
*   **Cadastro de Alunos:** Adição de novos registros de alunos com informações detalhadas, incluindo matrícula, nome, notas e dados de endereço (com preenchimento automático de CEP via ViaCEP).
*   **Listagem de Alunos:** Visualização de todos os alunos cadastrados em formato de tabela, com opções de busca e filtragem.
*   **Edição de Alunos:** Modificação de informações de alunos existentes.
*   **Exclusão de Alunos:** Remoção de registros de alunos do sistema.
*   **Dashboard Interativo:** Análise de dados dos alunos, incluindo métricas como total de alunos, maior e menor média, média geral, e um gráfico de distribuição das médias com curva de sino.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
.
├── app.py
├── auth.py
└── modules/
    ├── __pycache__/
    ├── adicionar.py
    ├── deletar.py
    ├── editar.py
    ├── home.py
    └── listar.py
```

*   `app.py`: Arquivo principal da aplicação Streamlit, responsável pela navegação entre as diferentes seções do sistema (Home, Adicionar, Listar, Editar, Deletar) e pelo fluxo de autenticação.
*   `auth.py`: Módulo responsável pela gestão de usuários, incluindo a criação da tabela de usuários, cadastro de novos usuários e verificação de credenciais de login, utilizando SQLite para armazenamento e SHA256 para hash de senhas.
*   `modules/`:
    *   `adicionar.py`: Contém a lógica para adicionar novos alunos ao banco de dados, incluindo a integração com a API ViaCEP para preenchimento automático de endereço.
    *   `deletar.py`: Implementa a funcionalidade de exclusão de alunos com base na matrícula ou nome.
    *   `editar.py`: Permite a edição dos dados de um aluno existente.
    *   `home.py`: Exibe a página inicial do sistema e o dashboard interativo com análises das notas dos alunos.
    *   `listar.py`: Responsável por exibir a lista de todos os alunos cadastrados.

## Tecnologias Utilizadas

*   **Python 3.x**
*   **Streamlit:** Framework para criação de aplicações web interativas.
*   **SQLite3:** Banco de dados leve para armazenamento local de dados de alunos e usuários.
*   **Pandas:** Biblioteca para manipulação e análise de dados.
*   **Numpy:** Biblioteca para computação numérica.
*   **Plotly:** Biblioteca para criação de gráficos interativos (utilizado no dashboard).
*   **Requests:** Biblioteca para fazer requisições HTTP (utilizado para integração com ViaCEP).
*   **Hashlib:** Módulo para operações de hashing seguro (utilizado para senhas).
*   **Streamlit-Option-Menu:** Componente Streamlit para criação de menus de navegação.

## Como Executar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado em seu sistema.

### 1. Clonar o Repositório

```bash
git clone <https://github.com/eduliradossantos/cadastro_de_alunos_streamlit.git>
cd <cadastro_de_alunos_stream>
```

### 2. Criar e Ativar um Ambiente Virtual (Recomendado)

```bash
python -m venv venv
# No Windows
.\venv\Scripts\activate
# No macOS/Linux
source venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

**Nota:** Se o arquivo `requirements.txt` não estiver presente, você pode criá-lo com as seguintes dependências:

```
streamlit
streamlit-option-menu
pandas
numpy
plotly
requests
```

### 4. Executar a Aplicação Streamlit

```bash
streamlit run app.py
```

Após executar o comando, a aplicação será aberta automaticamente em seu navegador padrão. Se não abrir, copie e cole o URL fornecido no terminal (geralmente `http://localhost:8501`).

### 5. Acesso ao aplicativo via Playground Streamlit

Caso queira acessar via Playground Streamlit, basta acessar `https://eduardolira-cadastrodealunos.streamlit.app/`
## Uso do Sistema

1.  **Login/Cadastro:** Ao iniciar a aplicação, você será direcionado para a tela de login. Você pode fazer login com um usuário existente ou cadastrar um novo usuário.
2.  **Navegação:** Após o login, utilize o menu lateral para navegar entre as funcionalidades: Home, Adicionar, Listar, Editar e Deletar.
3.  **Cadastro de Alunos:** Na seção "Adicionar", preencha os dados do aluno. Ao digitar o CEP, o logradouro, bairro, cidade e estado serão preenchidos automaticamente.
4.  **Dashboard:** Na seção "Home", expanda o "Dashboard" para visualizar as métricas e o gráfico de distribuição das médias dos alunos.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a Apache License. Veja o arquivo `LICENSE` para mais detalhes.

## Agradecimentos

Agradecemos ao Professor André Ribeiro pela orientação e à Escola Técnica Estadual Porto Digital pelo suporte no projeto COMPET Médio SophIA.


