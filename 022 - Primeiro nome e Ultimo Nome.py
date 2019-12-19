'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o ultimo nome separadamente.
Ex: Ana Maria de souza
primeiro = Ana
ultimo = souza
'''

nomeCompleto = str(input("Informe o nome completo:")).strip()
nome = nomeCompleto.split()
print("O primeiro nome é:{}".format(nome[0]))
print("O ultimo nome que aparece é: {}".format(nome[len(nome)-1])) 
