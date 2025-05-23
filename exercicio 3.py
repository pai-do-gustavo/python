# Importa a constante pi da biblioteca math (opcional, poderia usar 3.14159 diretamente)
import math

# Solicita o raio ao usuário (como inteiro)
raio = int(input("Digite o raio do círculo (número inteiro): "))

# Define o valor de pi
pi = 3.14159  # Também poderia usar math.pi para maior precisão

# Calcula diâmetro, circunferência e área
diametro = 2 * raio
circunferencia = 2 * pi * raio
area = pi * (raio ** 2)  # raio ao quadrado

# Exibe os resultados
print(f"Diâmetro: {diametro}")
print(f"Circunferência: {circunferencia:.2f}")  # Arredonda para 2 casas decimais
print(f"Área: {area:.2f}")