# faça um algoritmo que leia a idade de 5 pessaos
# e escreva quantas delas possuem idades iguais a 21 anos.
def verificaIdade21(idade1, idade2, idade3, idade4, idade5):
    contaIdade = 0

    if(idade1 == 21):
        contaIdade += 1
    if (idade2 == 21):
        contaIdade += 1
    if (idade3 == 21):
        contaIdade += 1
    if (idade4 == 21):
        contaIdade += 1
    if (idade5 == 21):
        contaIdade += 1

        print(f'o numero de idades iguais a 21 sao de {contaIdade}')



def main():
    idade1 = int(input('digite a primeira idade numero'))
    idade2 = int(input('digite a segunda idade numero'))
    idade3 = int(input('digite a terceira idade numero'))
    idade4 = int(input('digite a quarta idade numero'))
    idade5 = int(input('digite a quinta idade numero'))

verificaIdade21(idade1, idade2, idade3, idade4, idade5)

if __name__ == '__main__':
    main()