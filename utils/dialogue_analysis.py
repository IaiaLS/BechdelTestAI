import re
import logging
from utils.gemini_client import gemini_model

def extract_dialogues(text: str):
    logging.debug("=== Iniciando extração de diálogos ===")
    # Suporte a formatos [Nome]: fala ou Nome: fala
    pattern = r'^(?:\[?([\wÀ-ÿ\s\-]+)\]?):\s*(.*)$'
    dialogues = []

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        match = re.match(pattern, line)
        if match:
            speaker = match.group(1).strip()
            speech = match.group(2).strip()
            dialogues.append({"speakers": [speaker], "text": speech})
            logging.debug(f"Diálogo encontrado - Speaker: {speaker}, Fala: {speech}")
        else:
            logging.debug(f"Linha ignorada (não bateu com padrão): {line}")

    logging.debug(f"Total de diálogos extraídos: {len(dialogues)}")
    return dialogues


logger = logging.getLogger(__name__)

def is_about_men(dialogue_text: str) -> bool:

    logger.debug(f"Analisando tema do diálogo com IA: {dialogue_text}")
    prompt = (
        f"Analise o seguinte diálogo e determine se ele é sobre um homem (homens, namorados, maridos, "
        f"relacionamentos amorosos etc.):\n\n"
        f"\"{dialogue_text}\"\n\n"
        f"Responda apenas com 'Sim' ou 'Não'."
    )

    try:
        response = gemini_model.generate_content(prompt)
        result = response.text.strip().lower()
        logger.debug(f"Resultado IA (sobre homens): {result}")
        return "sim" in result
    except Exception as e:
        logger.error(f"Erro ao analisar com IA: {e}")
        keywords = ["homem", "rapaz", "garoto", "namorado", "pai", "marido"]
        return any(k in dialogue_text.lower() for k in keywords)
