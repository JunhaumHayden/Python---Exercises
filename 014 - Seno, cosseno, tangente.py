'''Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e tangente
desse ângulo'''

import math
print("====================")
print("      ANGULO")
print("====================")
angulo = float(input("Informe um ângulo:"))
print("====================")
seno = math.sin(math.radians(angulo))
print("O ângulo de {} tem SENO de {:.2f}".format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print("O ângulo de {} tem COSSENO de {:.2f}".format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print("O ângulo de {} tem TANGENTE de {:.2f}".format(angulo, tangente))
