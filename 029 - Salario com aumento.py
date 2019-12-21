'''
Escreva um programa que pergunte o salário
de um funcionário e calcule o valor do seu
aumneto. Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para os inferiores ou
iguais, o aumento é de 15%.
'''

salario = float(input("Informe o seu salário: R$"))
if salario > 1250:
    aumento = salario + (salario * 0.1)
    print("O seu salário atual é: R${}".format(salario))
    print("Com o reajuste ficou: R${:.2f}".format(aumento))
else:
    aumento = salario + (salario * 0.15)
    print("O seu salário atual é: R${}".format(salario))
    print("Com o reajuste ficou: R${:.2f}".format(aumento))
