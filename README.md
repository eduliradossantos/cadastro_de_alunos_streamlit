# Sistema de Cadastro de Alunos - COMPET Médio SophIA

Este repositório contém o trabalho de conclusão do Módulo 2 - Streamlit do projeto COMPET Médio SophIA, desenvolvido na Escola Técnica Estadual Porto Digital. O sistema é uma aplicação web interativa para cadastro e gerenciamento de alunos, construída utilizando a biblioteca Streamlit do Python.

## Sobre o Projeto

O projeto COMPET Médio SophIA visa capacitar estudantes para criação de agente de IA com Streamlit e Langchein. Este módulo, focado em Streamlit, permitiu a criação de uma ferramenta prática para a gestão de dados de alunos, incluindo funcionalidades de login, cadastro, listagem, edição e exclusão de registros, além de um dashboard interativo para visualização de dados.

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
*   **Agente de IA:** Faça upload de documentos de texto e planilhas e converse com eles.

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
    ├── listar.py
    └── agenteia.py
└── utils/
    ├── file_loader.py
    ├── limpar_resposta.py
    └── qa_chain_groq.py
```

*   `app.py`: Arquivo principal da aplicação Streamlit, responsável pela navegação entre as diferentes seções do sistema (Home, Adicionar, Listar, Editar, Deletar) e pelo fluxo de autenticação.
*   `auth.py`: Módulo responsável pela gestão de usuários, incluindo a criação da tabela de usuários, cadastro de novos usuários e verificação de credenciais de login, utilizando SQLite para armazenamento e SHA256 para hash de senhas.
*   `modules/`:
    *   `adicionar.py`: Contém a lógica para adicionar novos alunos ao banco de dados, incluindo a integração com a API ViaCEP para preenchimento automático de endereço.
    *   `deletar.py`: Implementa a funcionalidade de exclusão de alunos com base na matrícula ou nome.
    *   `editar.py`: Permite a edição dos dados de um aluno existente.
    *   `home.py`: Exibe a página inicial do sistema e o dashboard interativo com análises das notas dos alunos.
    *   `listar.py`: Responsável por exibir a lista de todos os alunos cadastrados.
    *   `agenteia.py`: Responsável por implementar os utils usando Groq e Langchain para executar conversa com IA.

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
git clone https://github.com/eduliradossantos/cadastro_de_alunos_streamlit.git
cd cadastro_de_alunos_stream
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
aiohappyeyeballs==2.6.1
aiohttp==3.12.15
aiosignal==1.4.0
altair==5.5.0
annotated-types==0.7.0
anyio==4.10.0
attrs==25.3.0
blinker==1.9.0
cachetools==6.2.0
certifi==2025.8.3
charset-normalizer==3.4.3
click==8.2.1
colorama==0.4.6
dataclasses-json==0.6.7
distro==1.9.0
et_xmlfile==2.0.0
faiss-cpu==1.12.0
filelock==3.19.1
frozenlist==1.7.0
fsspec==2025.9.0
gitdb==4.0.12
GitPython==3.1.45
greenlet==3.2.4
groq==0.31.1
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
httpx-sse==0.4.1
huggingface-hub==0.34.5
idna==3.10
Jinja2==3.1.6
jiter==0.10.0
joblib==1.5.2
jsonpatch==1.33
jsonpointer==3.0.0
jsonschema==4.25.1
jsonschema-specifications==2025.9.1
langchain==0.3.27
langchain-community==0.3.29
langchain-core==0.3.75
langchain-groq==0.3.8
langchain-text-splitters==0.3.11
langsmith==0.4.27
load-dotenv==0.1.0
MarkupSafe==3.0.2
marshmallow==3.26.1
mpmath==1.3.0
multidict==6.6.4
mypy_extensions==1.1.0
narwhals==2.4.0
networkx==3.5
numpy==2.3.3
openai==1.107.0
openpyxl==3.1.5
orjson==3.11.3
packaging==25.0
pandas==2.3.2
pillow==11.3.0
plotly
propcache==0.3.2
protobuf==6.32.0
pyarrow==21.0.0
pydantic==2.11.7
pydantic-settings==2.10.1
pydantic_core==2.33.2
pydeck==0.9.1
PyPDF2==3.0.1
python-dateutil==2.9.0.post0
python-dotenv==1.1.1
pytz==2025.2
PyYAML==6.0.2
referencing==0.36.2
regex==2025.9.1
requests==2.32.5
requests-toolbelt==1.0.0
rpds-py==0.27.1
safetensors==0.6.2
scikit-learn==1.7.2
scipy==1.16.2
sentence-transformers==5.1.0
setuptools==80.9.0
six==1.17.0
smmap==5.0.2
sniffio==1.3.1
SQLAlchemy==2.0.43
streamlit==1.49.1
streamlit-option-menu
sympy==1.14.0
tenacity==9.1.2
threadpoolctl==3.6.0
tiktoken==0.11.0
tokenizers==0.22.0
toml==0.10.2
torch==2.8.0
tornado==6.5.2
tqdm==4.67.1
transformers==4.56.1
typing-inspect==0.9.0
typing-inspection==0.4.1
typing_extensions==4.15.0
tzdata==2025.2
urllib3==2.5.0
watchdog==6.0.0
yarl==1.20.1
zstandard==0.24.0
```

### 4. Executar a Aplicação Streamlit

```bash
streamlit run app.py
```

Após executar o comando, a aplicação será aberta automaticamente em seu navegador padrão. Se não abrir, copie e cole o URL fornecido no terminal (geralmente `http://localhost:8501`).

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


