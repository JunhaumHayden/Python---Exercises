'''
Crie um programa que leia o nome de uma pessoa e diga
se ela tem "Silva" no nome.
'''

nomePessoa = str(input("Informe o seu nome:"))
print("Seu nome tem Silva?{}".format('SILVA' in nomePessoa.upper()))
