'''Um professor quer sortear um dos seus quatro alunos para
apagar o quadro. Faça um programa que ajude ele, lendo o
nome deles e escrevendo o nome do escolhido'''

import random
aluno1 = str(input("Informe o primeiro aluno:"))
aluno2 = str(input("Informe o segundo aluno:"))
aluno3 = str(input("Informe o terceiro aluno:"))
aluno4 = str(input("Informe o quarto aluno:"))
lista = [aluno1, aluno2, aluno3, aluno4]
alunoescolhido = random.choice(lista)
print("O aluno escolhido foi: {}".format(alunoescolhido))
