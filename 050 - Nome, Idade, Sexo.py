'''
Desenvolva um programa que leia o nome, idade
e sexo de 4 pessoas. No final do programa, mostre:

- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos
'''
mediaIdade = 0
HomemMaisVelho = 0
nomeVelho = ' '
totalM = 0
totalMulheres = 0
somaIdade = 0
for pessoa in range(1,6):
    nome = str(input("{}º - Informe o seu nome:".format(pessoa)))
    idade = int(input("{}º - Informe a sua idade:".format(pessoa)))
    sexo = str(input("{}º - Informe o seu sexo:[M/F] ".format(pessoa)))
    print("="*30)
    somaIdade = somaIdade + idade
    if pessoa == 1 and sexo == "Mm":
        HomemMaisVelho = idade
        nomeVelho = nome
    if sexo in "Mm" and idade > HomemMaisVelho:
        HomemMaisVelho = idade
        nomeVelho = nome
    if sexo in "Ff" and idade < 20:
        totalMulheres = totalMulheres + 1
mediaIdade = somaIdade / 4
print("A média de idade do grupo é: {}".format(mediaIdade))
print("O nome do homem mais velho é:{} e tem {} anos".format(nomeVelho,HomemMaisVelho))
print("Total de Mulheres: {}".format(totalMulheres))
