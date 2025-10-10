def classificacaoInmetro(inmetro):
    match inmetro:
        case ("D"):
            print(f"Ineficiente")
        case ("C"):
            print(f"Pouco Eficiente")
        case ("B"):
            print(f"Eficiente")
        case ("A"):
            print(f"Muito Eficiente")

        case _:
            print(f"Inmetro {inmetro} não encontrado")


def main():
    print("Digite uma letra de A até D")
    inmetro = str(input())

    classificacaoInmetro(inmetro)

if __name__ == "__main__":
    main() 
