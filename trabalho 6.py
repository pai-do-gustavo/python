
def calculodaTabuada(numero):
   multiplicacao1 = numero * 1
   multiplicacao2 = numero * 2
   multiplicacao3 = numero * 3
   multiplicacao4 = numero * 4
   multiplicacao5 = numero * 5
   multiplicacao6 = numero * 6
   multiplicacao7 = numero * 7
   multiplicacao8 = numero * 8
   multiplicacao9 = numero * 9
   multiplicacao10 = numero * 10


   resultado = multiplicacao1, multiplicacao2, multiplicacao3, multiplicacao4, multiplicacao5, multiplicacao6, multiplicacao7, multiplicacao8, multiplicacao9, multiplicacao10


   return resultado




numero = int(input('digite o numero:' ))


tabuada = calculodaTabuada(numero)


print(tabuada)