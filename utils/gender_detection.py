import os
import logging
from dotenv import load_dotenv
import google.generativeai as genai


logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")


load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
if not gemini_key:
    raise EnvironmentError("Chave GEMINI_API_KEY não encontrada no ambiente.")

genai.configure(api_key=gemini_key)
gemini_model = genai.GenerativeModel("gemini-2.5-flash")
logging.info("Gemini configurado com sucesso.")


def detect_explicit_gender(text: str):
    logging.debug(f"Analisando texto: {text}")
    prompt = (
        f"Analise a seguinte frase e determine o gênero explicitamente auto declarado:\n\n"
        f"\"{text}\"\n\nResponda apenas com: Feminino, Masculino, Não-binárie ou Nenhum."
    )
    try:
        response = gemini_model.generate_content(prompt)
        result = response.text.strip()
        logging.debug(f"Resposta Gemini: {result}")

        if any(g in result.lower() for g in ["feminino", "mulher"]):
            return "Feminino"
        elif any(g in result.lower() for g in ["masculino", "homem"]):
            return "Masculino"
        elif "não" in result.lower():
            return "Não-binárie"
        elif "nenhum" in result.lower():
            return None
        else:
            return None
    except Exception as e:
        logging.error(f"Erro no Gemini: {e}")
        return None


def infer_gender_by_name(name: str):
    logging.debug(f"Inferindo gênero pelo nome: {name}")
    prompt = (
        f"Determine se o nome '{name}' geralmente é associado a um gênero específico "
        f"e responda apenas com: Feminino, Masculino, Não-binárie ou Desconhecido."
    )
    try:
        response = gemini_model.generate_content(prompt)
        result = response.text.strip()
        logging.debug(f"Resposta Gemini: {result}")

        if "feminino" in result.lower():
            return "Feminino"
        elif "masculino" in result.lower():
            return "Masculino"
        elif "não" in result.lower():
            return "Não-binárie"
        else:
            return "Desconhecido"
    except Exception as e:
        logging.error(f"Erro no Gemini: {e}")
        return "Desconhecido"
