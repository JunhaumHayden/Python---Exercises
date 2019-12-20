'''
Escreva um programa que leia a velocidade de um
carro. Se ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar
R$7,00 por cada Km acima do limite.
'''

print("="*20)
print("VELOCIDADE DE CARROS:")
print("="*20)
velocidade = float(input("Informe a velocidade do carro:"))
if velocidade > 80:
    print("O carro ultrapassou 80Km/h")
    print("="*28)
    print("O carro foi multado!!!")
    print("="*28)
else:
    print("O carro não ultrapassou 80km/h")
    print("="*28)
    print("O carro não foi multado!!!")
    print("="*28)
