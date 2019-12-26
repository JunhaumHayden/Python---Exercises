'''
Faça um programa que leia um número
qualquer e mostre o seu fatorial.
Ex.: 5! = 5x4x3x3x1 =120
'''

numero = int(input("Informe um número:"))
fatorial = 1
print("Fatorial de {}!".format(numero))
while numero > 0:
    print("{}".format(numero), end=" ")
    print("x " if numero > 1 else "= ", end="")
    fatorial = fatorial * numero
    numero = numero - 1
print("{}".format(fatorial))
    
