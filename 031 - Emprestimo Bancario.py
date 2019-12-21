'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. Pergunte o valor da casa, o
salário do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou
então o emprestimo será negado.
'''

valorCasa = float(input("Informe o preço da casa:R$"))
salario = float(input("Informe o seu salário: R$"))
anos = float(input("Em quantos anos vocÊ deseja pagar:"))

prestacao = valorCasa / (anos * 12)
print("O valor da prestação será de: R${}".format(prestacao))
prestacaoM = salario * 0,3
if prestacao <= prestacaoM:
    print("Emprestimo Negado!")
else:
    print("Empréstimo Confirmado!")



