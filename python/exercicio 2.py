# Solicita o número de 5 dígitos
numero = input("Digite um número de 5 dígitos: ")

# Verifica se o número tem exatamente 5 dígitos
if len(numero) != 5 or not numero.isdigit():
    print("Por favor, digite um número válido com exatamente 5 dígitos.")
else:
    # Separa e imprime cada dígito com três espaços
    for digito in numero:
        print(digito + "   ")  # Três espaços após cada dígito