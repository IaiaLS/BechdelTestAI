import logging
from collections import Counter
from utils.dialogue_analysis import extract_dialogues
from utils.gender_detection import detect_explicit_gender, infer_gender_by_name

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def analyze_text(text):
    logger.debug("=== Iniciando análise de texto ===")
    logger.debug(f"Texto recebido:\n{text}")

    dialogues = extract_dialogues(text)
    logger.debug(f"Diálogos extraídos: {dialogues}")

    characters_gender = {}

    for d in dialogues:
        for speaker in d["speakers"]:

            if speaker not in characters_gender:

                explicit_gender = detect_explicit_gender(d["text"])
                logger.debug(f"Fala analisada ({speaker}): {d['text']}")
                logger.debug(f"Gênero explícito identificado: {explicit_gender}")

                if explicit_gender:
                    characters_gender[speaker] = explicit_gender
                else:
                    characters_gender[speaker] = infer_gender_by_name(speaker)


    characters_by_gender = Counter(characters_gender.values())
    logger.debug(f"Mapa final de personagens/gênero: {characters_gender}")
    logger.debug(f"Contagem de personagens por gênero: {characters_by_gender}")


    speech_by_gender = Counter()
    for d in dialogues:
        word_count = len(d["text"].split())
        for speaker in d["speakers"]:
            gender = characters_gender.get(speaker, "Desconhecido")
            speech_by_gender[gender] += word_count

    logger.debug(f"Distribuição de falas por gênero: {speech_by_gender}")
    logger.debug("=== Análise concluída ===")

    return {
        "characters_by_gender": characters_by_gender,
        "speech_by_gender": speech_by_gender,
        "dialogues": dialogues,
        "characters_gender": characters_gender
    }