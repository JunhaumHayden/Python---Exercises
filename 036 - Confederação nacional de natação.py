'''
A Confederação Nacional de Natação precisa de um
programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIN
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 25 anos: SENIOR
Acima: MASTER
'''

from datetime import date
AnoAtual = date.today().year
nascimento = int(input("Informe o ano de nascimento:"))
idade = AnoAtual - nascimento
print("A sua idade é: {}".format(idade))
if idade < 9:
    print("A sua categoria é: MIRIN!!")
elif idade > 9 and idade < 14:
    print("A sua categoria é: INFANTIL!!")
elif idade > 14 and idade < 19:
    print("A sua categoria é: JUNIOR!!")
elif idade > 19 and idade < 25:
    print("A sua categoria é: SÊNIOR!!")
elif idade > 25:
    print("A sua categoria é: MASTER!!")
