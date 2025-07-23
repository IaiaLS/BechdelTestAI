from utils.gender_detection import detect_explicit_gender, infer_gender_by_name

def run_tests():
    print("=== Testando detect_explicit_gender ===")
    textos = [
        "Sou uma mulher trans e uso pronomes ela/dela",
        "Eu sou homem e meu pronome é ele",
        "Me identifico como não-binárie",
        "Meu pronome é elu",
        "Sem informação explícita"
    ]
    for t in textos:
        print(f"Texto: {t}\n→ Resultado: {detect_explicit_gender(t)}\n")

    print("=== Testando infer_gender_by_name ===")
    nomes = ["Ana", "João", "Alex", "Juliana", "Gabriel", "Sam"]
    for n in nomes:
        print(f"Nome: {n}\n→ Resultado: {infer_gender_by_name(n)}\n")


if __name__ == "__main__":
    run_tests()
