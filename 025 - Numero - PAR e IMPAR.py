'''
Crie um programa que leia um número inteiro
e mostre na tela se ele é PAR ou IMPAR.
'''

print("="*20)
print("    PAR | IMPAR")
print("="*20)
numero = int(input("Informe um número: "))
print("="*20)
if numero % 2 == 0:
    print("O número {} é PAR!!!".format(numero))
else:
    print("O número {} é IMPAR!!!".format(numero))
