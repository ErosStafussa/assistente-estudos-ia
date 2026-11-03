
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.ia import gerar_resposta
from app.database import supabase



app = FastAPI()


class PerguntaRequest(BaseModel):
    pergunta: str = Field(
        min_length=3,
        max_length=1000
    )


@app.get("/")
def inicio():
    return {
        "mensagem": "Assistente de Estudos com IA funcionando!"
    }


@app.get("/historico")
def ver_historico():
    resultado = (
        supabase.table("mensagens")
        .select("*")
        .order("id")
        .execute()
    )

    return {
        "historico": resultado.data
    }


@app.delete("/historico")
def limpar_historico():
    supabase.table("mensagens").delete().gte("id", 1).execute()

    return {
        "mensagem": "Histórico apagado com sucesso!"
    }


@app.post("/chat")
def chat(dados: PerguntaRequest):

    resultado = (
        supabase.table("mensagens")
        .select("*")
        .order("id")
        .execute()
    )

    contexto = ""

    for mensagem in resultado.data:
        contexto += (
            f"{mensagem['papel']}: "
            f"{mensagem['conteudo']}\n"
        )

    prompt = f"""
    Você é um assistente de estudos.

    Histórico da conversa:
    {contexto}

    Nova pergunta do usuário:
    {dados.pergunta}
    """

    try:
        resposta = gerar_resposta(prompt)

    except RuntimeError:
        raise HTTPException(
            status_code=503,
            detail="Serviço de IA indisponível. Tente novamente."
        )

    gravacao = supabase.table("mensagens").insert([
        {
            "papel": "Usuário",
            "conteudo": dados.pergunta
        },
        {
            "papel": "Assistente",
            "conteudo": resposta
        }
    ]).execute()



    return {
    "sua_pergunta": dados.pergunta,
    "resposta": resposta,
    "mensagens_salvas": gravacao.data
}