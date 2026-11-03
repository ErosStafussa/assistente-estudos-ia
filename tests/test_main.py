
from fastapi.testclient import TestClient
from app.main import app, historico

client = TestClient(app)


def setup_function():
    historico.clear()


def test_inicio():
    resposta = client.get("/")
    assert resposta.status_code == 200


def test_chat(monkeypatch):
    def resposta_falsa(prompt):
        return "Python é uma linguagem de programação."

    monkeypatch.setattr("app.main.gerar_resposta", resposta_falsa)

    resposta = client.post(
        "/chat",
        json={"pergunta": "O que é Python?"}
    )

    assert resposta.status_code == 200
    assert "Python" in resposta.json()["resposta"]


def test_historico():
    historico.append({
        "papel": "Usuário",
        "conteudo": "Olá"
    })

    resposta = client.get("/historico")

    assert resposta.status_code == 200
    assert len(resposta.json()["historico"]) == 1


def test_limpar_historico():
    historico.append({
        "papel": "Usuário",
        "conteudo": "Olá"
    })

    resposta = client.delete("/historico")

    assert resposta.status_code == 200
    assert len(historico) == 0


def test_pergunta_curta():
    resposta = client.post(
        "/chat",
        json={"pergunta": "Oi"}
    )

    assert resposta.status_code == 422
