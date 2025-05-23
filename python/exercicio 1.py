# Solicita dois números inteiros ao usuário
numeros = []
for i in range(1, 3):
    num = int(input(f"Digite o {i}º número inteiro: "))
    numeros.append(num)

num1, num2 = numeros  # Desempacota os números

# Calcula as operações
operacoes = {
    "Soma": f"{num1} + {num2} = {num1 + num2}",
    "Produto": f"{num1} * {num2} = {num1 * num2}",
    "Diferença": f"{num1} - {num2} = {num1 - num2}",
    "Quociente (divisão)": f"{num1} / {num2} = {(num1 / num2):.2f}"
}

# Exibe os resultados iterando sobre o dicionário de operações
for nome, resultado in operacoes.items():
    print(f"{nome}: {resultado}")