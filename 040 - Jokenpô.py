'''
Crie um programa que faça o computador
jogar Jokenpô com você.
'''

from random import randint
from time import sleep
mao = ('Pedra', 'Tesoura','Papel')
computador = randint(0,2)
print('='*20)
print("      JOKENPÔ")
print('='*20)
print("""Suas opções:
[0] - Pedra
[1] - Tesoura
[2] - Papel
""")
print('JOGUE AGORA!!!')
sleep(2)
jogador = int(input('Escolha uma Jogada:'))
print("="*30)
print('O computador escolheu: {}'.format(mao[computador]))
print('O jogador escolheu: {}'.format(mao[jogador]))
print("="*30)
print("O VENCEDOR DA PARTIDA É:")
sleep(2)
if computador == 0:
    if jogador == 0:
        print("Não temos vencedor deu:")
        print("EMPATE!!!")
    elif jogador == 1:
        print("O computador VENCEU!!!")
        print("E O JOGADOR PERDEU!!!")
    elif jogador == 2:
        print("O COMPUTADOR PERDEU!!!")
        print("O JOGADOR VENCEU!!!")
elif computador == 1:
    if jogador == 0:
        print("O COMPUTADOR PERDEU!!!")
        print("O JOGADOR VENCEU!!!")
    elif jogador == 1:
        print("Não temos vencedor deu:")
        print("EMPATE!!!")
    elif jogador == 2:
        print("O COMPUTADOR VENCEU!!!")
        print("O JOGADOR PERDEU!!!")
elif computador == 2:
    if jogador == 0:
        print("O COMPUTADOR VENCEU!!!") 
        print("O JOGADOR PERDEU!!!")
    elif jogador == 1:
        print("O COMPUTADOR PERDEU!!!")
        print("O JOGADOR VENCEU!!!")
    elif jogador == 2:
        print("Não temos vencedor deu:")
        print("EMPATE!!!")
        
