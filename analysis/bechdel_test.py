from utils.dialogue_analysis import is_about_men


def bechdel_test(analysis_result):
    dialogues = analysis_result["dialogues"]
    characters_gender = analysis_result["characters_gender"]

    female_characters = [c for c, g in characters_gender.items() if g == "Feminino"]

    if len(female_characters) < 2:
        return {"passes": False, "reason": "Menos de duas personagens femininas"}

    women_dialogues = [
        d for d in dialogues
        if all(s in female_characters for s in d["speakers"])
    ]

    if not women_dialogues:
        return {"passes": False, "reason": "Não há diálogo entre mulheres"}

    for d in women_dialogues:
        if not is_about_men(d["text"]):
            return {"passes": True, "reason": "Passa no teste de Bechdel"}

    return {"passes": False, "reason": "Diálogos entre mulheres são sobre homens"}
