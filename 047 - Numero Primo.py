'''
Faça um programa que leia um número
inteiro e diga se ele é ou não um
número primo
'''
total = 0
numero = int(input("Informe um número: "))
for primo in range(1,numero):
    if primo % numero == 0:
        print(numero)
        total = total +1
    else:
       print(numero)
if total == 2:
    print("O número é PRIMO!")
else:
    print("O número não é PRIMO!")
