# Calculadora de IMC (Índice de Massa Corporal)
print("=== CALCULADORA DE IMC ===")

# Entrada de dados
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Classificação (OMS)
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    classificacao = "Peso normal"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
elif 30 <= imc < 35:
    classificacao = "Obesidade Grau I"
elif 35 <= imc < 40:
    classificacao = "Obesidade Grau II"
else:
    classificacao = "Obesidade Grau III (mórbida)"

# Resultados
print(f"\nSeu IMC é {imc:.1f}")
print(f"Classificação: {classificacao}")

# Tabela de referência
print("\n=== TABELA DE CLASSIFICAÇÃO (OMS) ===")
print("Abaixo de 18.5: Abaixo do peso")
print("18.5 - 24.9: Peso normal")
print("25.0 - 29.9: Sobrepeso")
print("30.0 - 34.9: Obesidade Grau I")
print("35.0 - 39.9: Obesidade Grau II")
print("Acima de 40: Obesidade Grau III (mórbida)")