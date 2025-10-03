def verificaDivisibilidade(numero):
    if numero % 5 == 0 or numero % 3 == 0:
        print(f"O número {numero} é divisível por 5 ou 3.")
    else:
        print(f"O número {numero} não é divisível por 5 nem por 3.")

numero = int(input("Digite um número inteiro: "))
verificaDivisibilidade(numero)