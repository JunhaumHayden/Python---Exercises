'''
Escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peca para o usuario tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuario venceu
ou perdeu.
'''

from random import randint
from time import sleep
numero = randint(0,5)
print("="*19)
print("PENSE EM UM NÚMERO:")
print("="*19)
num = int(input("Informe um número:"))
print("PENSANDO:")
sleep(3)
if num == numero:
    print("O jogador venceu!!!")
else:
    print("O jogador perdeu!!!")
    print("O número escolhido foi: {} e você escolheu {}".format(numero, num))

