'''
Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos digitos separados.
Ex.:
Digite um número: 1845
unidade:5 dezena:4 centena:8 milhar:1
'''

numero = int(input("Informe um número:"))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print("A unidade do número {} é: {}".format(numero,unidade))
print("A dezena do número {} é: {}".format(numero,dezena))
print("A centena do número {} é {}".format(numero,centena))
print("A milhar do número {} é {}".format(numero, milhar))
