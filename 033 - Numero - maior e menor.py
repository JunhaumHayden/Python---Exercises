'''
Escreva um programa que leia dois números inteiros
e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é menor
- Não existe valor maior, os dois são iguais
'''

print("="*20)
print("    MAIOR | MENOR")
print("="*20)
num1 = int(input("Informe o primeiro número:"))
num2 = int(input("Informe o segundo número:"))
if num1 > num2:
    print("O número {} é maior que o número {}".format(num1,num2))
elif num2 > num1:
    print("O número {} é maior que o número {}".format(num2,num1))
elif num1 == num2:
    print("O número {} e {} são iguais!".format(num1,num2))
