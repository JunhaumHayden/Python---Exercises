'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todos as letras maiúsculas e minusculas
Quantas letras ao todo (Sem considerar espaços)
Quantas letras tem o primeiro nome
'''

nomeCompleto = str(input("Informe o seu nome completo:"))
print("O seu nome em Maiúsculo é: {}".format(nomeCompleto.upper()))
print("O seu nome em Minusculo é: {}".format(nomeCompleto.lower()))
print("O seu nome possui {}letras ao todo".format(len(nomeCompleto)-nomeCompleto.count(' ')))
separa = nomeCompleto.split()
print("O primeiro nome tem {} letras".format(separa[0],len(separa[0])))
