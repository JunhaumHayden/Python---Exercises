'''
Desenvolva uma lógico que leia o peso e a altura
de uma pessoa, calcule seu IMC e mostre seu status,
de acordo a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
Acima de 40: Obesidade morbida
'''
print("="*20)
print("      IMC")
print("="*20)
peso = float(input("Informe o seu peso:"))
altura = float(input("Informe a sua altura: "))
IMC = peso / (altura*altura)
print("O seu IMC é:{:.2f}kg".format(IMC))
print()
if IMC < 18.5:
    print("ABAIXO DO PESO!!!")
elif  IMC > 18.5 and IMC < 25:
    print("PESO IDEAL!!!")
elif IMC > 25 and IMC < 30:
    print("SOBREPESO!!!")
elif IMC > 30 and IMC < 40:
    print("OBESIDADE!!!")
else:
    print("OBESIDADE MÓRBIDA!!!")
