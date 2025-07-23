import re
import logging

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

def extract_characters_with_gender(text):
    return {}  # TODO: implementar

def is_about_men(text):
    return False  # TODO: implementar
