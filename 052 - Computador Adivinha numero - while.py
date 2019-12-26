'''
O computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para
vencer
'''

from random import randint

computador = randint(0,10)
print("Adivinhe o número: ")
acertar = False
while not acertar:
    numero = int(input("Informe o seu número:"))
    if numero == computador:
        acertar = True
        print("Você acertou o número!!!")
        print("Computador {} e Você {}".format(computador,numero))
    else:
        if computador > numero:
            print("Tente um número MAIOR!!!")
        elif computador < numero:
            print("Tente um número MENOR!!!")
        else:
            print("Você errou o número!!!")

