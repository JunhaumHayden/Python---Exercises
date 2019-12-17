'''Crie um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostre quantos
Dolares ela pode comprar'''

print("=====================")
print("CONVERSÃO EM DOLARES")
print("=====================")
dinheiro = float(input("Quanto você possui na carteira: R$ "))
print()
print(" Você tem R${} na carteira".format(dinheiro))
dolar = dinheiro*3.27
print(" Você tem US${} na carteira".format(dolar))
