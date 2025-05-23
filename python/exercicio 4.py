# Calculadora de Pegada de Carbono (versão simplificada)
print("=== CALCULADORA DE EMISSÃO DE CARBONO ===")

# Fatores de emissão (valores aproximados em kg CO2 por unidade)
FATOR_ELETRICIDADE = 0.5   # kg CO2 por kWh
FATOR_GASOLINA = 2.31      # kg CO2 por litro
FATOR_GAS_NATURAL = 2.0    # kg CO2 por m³

# Entrada de dados do usuário
kwh = float(input("Digite seu consumo mensal de eletricidade (kWh): "))
litros_gasolina = float(input("Digite o consumo mensal de gasolina (litros): "))
m3_gas = float(input("Digite o consumo mensal de gás natural (m³): "))

# Cálculos
emissao_eletricidade = kwh * FATOR_ELETRICIDADE
emissao_gasolina = litros_gasolina * FATOR_GASOLINA
emissao_gas = m3_gas * FATOR_GAS_NATURAL

# Total de emissões
total_emissao = emissao_eletricidade + emissao_gasolina + emissao_gas

# Resultados
print("\n=== RESULTADOS ===")
print(f"Emissão por eletricidade: {emissao_eletricidade:.2f} kg CO2")
print(f"Emissão por gasolina: {emissao_gasolina:.2f} kg CO2")
print(f"Emissão por gás natural: {emissao_gas:.2f} kg CO2")
print(f"\nTOTAL MENSAL: {total_emissao:.2f} kg CO2")
print(f"TOTAL ANUAL: {total_emissao * 12:.2f} kg CO2")

# Comparação com a média global
media_global_anual = 4000  # kg CO2 per capita/ano (fonte: World Bank)
print(f"\nComparação com a média global anual ({media_global_anual} kg CO2):")
if total_emissao * 12 > media_global_anual:
    print("Você está acima da média. Considere reduzir seu consumo!")
else:
    print("Você está abaixo da média. Parabéns!")

