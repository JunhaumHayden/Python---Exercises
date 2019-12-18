'''Crie um program que leia um número real qualquer
pelo teclado e mostre na tela sua porção inteira
Ex.: Digite um número: 6.127
O número 6.127 tem a parte inteira 6'''

import math
print("=================")
print("  ARREDONDANDO")
print("=================")
numero = float(input("Informe um número:"))
print("O número digitado foi: {}".format(numero))
print("A sua parte inteira é: {}".format(math.trunc(numero)))
