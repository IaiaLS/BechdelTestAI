import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")
if not gemini_key:
    raise EnvironmentError("Chave GEMINI_API_KEY não encontrada no ambiente.")


genai.configure(api_key=gemini_key)


try:
    gemini_model = genai.GenerativeModel("gemini-2.0-flash")
    logger.info("Gemini configurado com sucesso.")
except Exception as e:
    logger.error(f"Erro ao configurar Gemini: {e}")
    gemini_model = None
