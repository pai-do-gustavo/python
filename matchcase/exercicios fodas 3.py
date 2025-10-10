def main():
    match mes:
        case 9:
            match dia:
                case 7:
                    print(f"dia {dia} e dia da independencia do brasil")
                case _:
                    print("este dia nao existe")
        case 10:
            match dia:
                case 12:
                    print(f"dia {dia} e dia das crianças")
                case _:
                    print("este dia nao existe")
        case _:
            print("esse mes nao existe")

    def main():
     mes = int(input("digite o mes:"))
     dia = int(input("digite um dia do mes:"))

    verificaferiado(mes, dia)

if __name__ == "__main__":
    main()