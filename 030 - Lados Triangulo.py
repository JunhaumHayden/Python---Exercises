'''
Desenvolva um programa que leia o comprimento de
trÊs retas e diga ao usuário se elas podem ou não
formar um triângulo.
'''

print("="*25)
print("        TRIÂNGULO")
print("="*25)

lado1 = float(input("Informe o primeiro lado:"))
lado2 = float(input("Informe o segundo lado:"))
lado3 = float(input("Informe o terceiro lado:"))
print()

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("O lados formam um TRIÂNGULO!")
else:
    print("Os lados não formam um TRIÂNGULO!")
