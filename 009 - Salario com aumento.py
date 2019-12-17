'''Faça um algoritmo que leia o salário de um
funcionário e mostre seu novo salário, com 15%
de aumento'''

num1 = float(input("Informe o salário do funcionário: R$"))
print("===============")
print("SALÁRIO ATUAL")
print("===============")
print()
print("O salário atual é: R${}".format(num1))
aumento = num1 + (num1*0.15)
print("===============")
print("SALÁRIO NOVO")
print("===============")
print()
print("O salário com aumento é: R${:.2f}".format(aumento))
