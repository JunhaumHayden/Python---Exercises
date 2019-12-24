'''
Faça um programa que leia o peso
de cinco pessoas. No final, mostre
qual foi o maior e menor pesos lidos.
'''
PesoMaior = 0
PesoMenor = 0
for peso in range(1,6):
    massa = int(input("Informe o seu peso:"))
    if peso == 1:
        PesoMaior = peso
        PesoMenor = peso
    else:
        if peso > PesoMaior:
            PesoMaior = peso
        if peso < PesoMenor:
            PesoMenor = peso
print("O maior peso é:{}kg".format(PesoMaior))
print("O menor peso é:{}kg".format(PesoMenor))
