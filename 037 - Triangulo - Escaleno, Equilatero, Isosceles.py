'''
Refaça o desafio dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
'''
print("="*20)
print("    TRIÂNGULO")
print("="*20)

lado1 = int(input("Informe o primeiro lado:"))
lado2 = int(input("Informe o segundo lado:"))
lado3 = int(input("Informe o terceiro lado:"))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Os lados formam um TRIÂNGULO!!!")
    if lado1 == lado2 == lado3:
        print("TRIÂNGULO EQUILÁTERO!")
    if lado1 == lado2 != lado3:
        print("TRIÂNGULO ISÓSCELES!")
    if lado1 != lado2 != lado3:
        print("TRIÂNGULO ESCALENO!")
else:
    print("Os lados não formam um TRIÂNGULO!!!")
