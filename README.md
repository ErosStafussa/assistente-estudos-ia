# Assistente de Estudos com IA

Esse projeto foi desenvolvido para praticar Python, criação de APIs e integração com inteligência artificial.

A ideia é ter um assistente que consiga responder dúvidas, explicar assuntos e ajudar nos estudos.

## Tecnologias utilizadas

- Python
- FastAPI
- Gemini API
- Supabase
- PostgreSQL
- Pytest

## Funcionalidades

- Enviar perguntas para a IA.
- Receber respostas sobre diferentes assuntos.
- Consultar o histórico de conversas.
- Salvar mensagens no banco de dados.
- Limpar o histórico.

## Como executar

Clone o repositório:

```bash
git clone https://github.com/ErosStafussa/assistente-estudos-ia.git
```

Entre na pasta:

```bash
cd assistente-estudos-ia
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente no Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto e adicione suas chaves:

```env
GEMINI_API_KEY=sua_chave
SUPABASE_URL=sua_url
SUPABASE_KEY=sua_chave
```

Inicie o servidor:

```bash
uvicorn app.main:app --reload
```

Acesse a documentação da API:

http://127.0.0.1:8000/docs

## Testes

Para executar os testes:

```bash
python -m pytest -v
```

## Sobre o projeto

Esse é um dos meus projetos de estudo na área de desenvolvimento backend. Foi desenvolvido para colocar em prática conhecimentos de Python, APIs, banco de dados e inteligência artificial.

