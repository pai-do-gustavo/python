def verificaNumero(numero):
    if numero == 0:
        print("É ZERO")
    elif numero > 0:
        print("O número é positivo.")
    else:
        print("O número é negativo.")

numero = int(input("Digite um número: "))
verificaNumero(numero)