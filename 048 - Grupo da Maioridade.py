'''
Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e
quantas já são maiores.
'''

print("="*33)
print("           MAIORIDADE")
print("="*33)
print()
from datetime import date
anoAtual = date.today().year
totalMaior = 0
totalMenor = 0
for pessoas in range(0,6):
    anoNascimento = int(input("Informe o seu Ano de Nascimento:"))
    idade = anoAtual - anoNascimento
    if idade >= 18:
        totalMaior = totalMaior + 1
    else:
       totalMenor = totalMenor + 1
print()
print("Total de pessoas maiores de idade:{}".format(totalMaior))
print("Total de pessoas com menor idade:{}".format(totalMenor))
