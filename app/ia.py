from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()


def gerar_resposta(prompt):

    try:
        resposta = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt
        )

        return resposta.output_text

    except Exception:
        raise RuntimeError("Não foi possível gerar uma resposta da IA.")