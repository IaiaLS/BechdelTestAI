import os
import logging
from utils.gemini_client import gemini_model



logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")



gemini_key = os.getenv("GEMINI_API_KEY")
if not gemini_key:
    raise EnvironmentError("Chave GEMINI_API_KEY não encontrada no ambiente.")

logging.info("Gemini configurado com sucesso.")


def detect_explicit_gender(text: str):
    logging.debug(f"Analisando texto: {text}")
    prompt = (
        f"Analise a seguinte frase e determine se quem fala auto declara o gênero explicitamente, diga qual, "
        f"senão vai na opção Nenhum:\n\n"
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
        f"Dado apenas o nome: '{name}' de uma pessoa, classifique o gênero mais provável"
        f"(considere que pode ser um nome famoso):  "
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
