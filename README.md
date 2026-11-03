# Assistente de Estudos com IA

Esse projeto é um assistente de estudos desenvolvido em Python. A ideia é permitir que o usuário faça perguntas e receba explicações usando inteligência artificial.

O projeto foi criado para praticar desenvolvimento Backend e integração com APIs de IA.

## Funcionalidades

- Fazer perguntas para a IA.
- Receber respostas usando o Gemini.
- Guardar o histórico da conversa.
- Consultar mensagens anteriores.
- Apagar o histórico.
- Validar as perguntas enviadas.
- Tratar erros na comunicação com a IA.

## Tecnologias utilizadas

- Python
- FastAPI
- Google Gemini API
- Pydantic
- Pytest
- HTTPX

## Como executar

1. Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

2. Entre na pasta do projeto:

```bash
cd assistente-estudos-ia
```

3. Crie e ative o ambiente virtual:

```bash
python -m venv .venv
```

```powershell
.venv\Scripts\Activate.ps1
```

4. Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

5. Crie um arquivo `.env` na pasta principal e adicione sua chave da Gemini:

```env
GEMINI_API_KEY=sua_chave_aqui
```

6. Inicie o projeto:

```bash
python -m uvicorn app.main:app --reload
```

Acesse a documentação da API pelo endereço:

http://127.0.0.1:8000/docs

## Testes

Para executar os testes automatizados:

```bash
python -m pytest -v
```

## Endpoints

| Método | Rota | Função |
|---|---|---|
| GET | `/` | Verifica se a API está funcionando |
| POST | `/chat` | Envia uma pergunta para a IA |
| GET | `/historico` | Mostra o histórico |
| DELETE | `/historico` | Apaga o histórico |

## Sobre o projeto

Esse foi um dos meus projetos de estudo para aprofundar meus conhecimentos em Python e Backend.

Durante o desenvolvimento, pratiquei criação de APIs, integração com inteligência artificial, organização de código e testes automatizados.

Ainda pretendo adicionar novas funcionalidades e conectar um banco de dados para armazenar as conversas.