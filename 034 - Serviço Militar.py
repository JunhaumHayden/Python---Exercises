'''
Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com sua idade, se ele ainda vai se
alistat ao serviço militar, se é a hora de se alistar ou
se já passou do tempo do alistamento. Seu programa também
deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
anoAtual = date.today().year
anoNascimento = int(input("Informe o ano de nascimento:"))
idade = anoAtual - anoNascimento
print("Você nasceu em:{}".format(anoNascimento))
print("E a sua idade é:{}".format(idade))
if idade < 18:
    print("Você com {} anos ainda vai se alistar!".format(idade))
    quantaFalta = 18 - idade
    print("Falta {}anos para se alistar!".format(quantaFalta))
elif idade == 18:
    print("Você com {} anos está na hora de se alistar!".format(idade))
elif idade > 18:
    print("Você com {} anos passou do tempo de se alistar!".format(idade))
    quantaFalta = idade - 18
    print("Já se passaram {} anos do seu alistamento!".format(quantaFalta))
    
