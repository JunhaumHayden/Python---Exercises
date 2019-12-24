'''
Desenvolva um programa que leia o primeiro
termo e a razão de uma PA. No final, mostre
10 primeiros termos dessa progressão.
'''

primeiroTermo = int(input("Informe o primeiro termo:"))
Razao = int(input("Informe a razão:"))
dezTermos = primeiroTermo + (10 - 1)*Razao
for Pa in range(primeiroTermo,dezTermos + Razao,Razao):
    print("{}".format(Pa), end=" ")
    
