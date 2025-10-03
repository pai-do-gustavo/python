def classificarProduto(codigo):
    if codigo == 1:
        print("Classificação: Alimento não-perecível")
    elif 2 <= codigo <= 4:
        print("Classificação: Alimento perecível")
    elif codigo == 5 or codigo == 6:
        print("Classificação: Vestuário")
    elif codigo == 7:
        print("Classificação: Higiene pessoal")
    elif 8 <= codigo <= 15:
        print("Classificação: Limpeza e utensílios domésticos")
    else:
        print("Código inválido")

codigo = int(input("Digite o código do produto: "))
classificarProduto(codigo)