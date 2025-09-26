def soma(numero1, numero2, numero3, numero4):
   total = 0


   if(numero1 % 2 == 0):
       total += numero1
   if (numero2 % 2 == 0):
       total += numero2
   if (numero3 % 2 == 0):
       total += numero3
   if (numero4 % 2 == 0):
       total += numero4


   return total


def contaPares(numero1, numero2, numero3, numero4):
   total = 0


   if(numero1 % 2 == 0):
       total += 1
   if (numero2 % 2 == 0):
       total += 1
   if (numero3 % 2 == 0):
       total += 1
   if (numero4 % 2 == 0):
       total += 1


   return total




def main():
   numero1 = int(input("Digite o primeira numero: "))
   numero2 = int(input("Digite o segunda numero: "))
   numero3 = int(input("Digite o terceira numero: "))
   numero4 = int(input("Digite o quarta numero: "))


   totalSoma = soma(numero1, numero2, numero3, numero4)
   totalPares = contaPares(numero1, numero2, numero3, numero4)
   media = totalSoma / totalPares
   print(f"A soma dos numeros é: {totalSoma}")
   print(f"A soma dos numeros é: {media}")




if __name__ == "__main__":
   main()
