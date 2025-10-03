def verificaDivisibilidade(numero):
    if numero % 2 == 0 and numero % 3 == 0:
        print(f"O número {numero} é divisível por 2 e 3.")
    else:
        print(f"O número {numero} não é divisível por 2 e 3.")

numero = int(input("Digite um número inteiro: "))
verificaDivisibilidade(numero)