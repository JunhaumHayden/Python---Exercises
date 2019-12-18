'''Faça um programa que leia o comprimento do
cateto oposto e do cateto adjacente de um triângulo
retângulo, calcule e mostre o comprimento da hipotenusa'''

import math
Co = float(input("Informe o lado do cateto oposto:"))
Ca = float(input("Informe o lado do cateto adjacente:"))
hipotenusa = math.hypot(Co,Ca)
print("A hipotenusa vale:{:.2f}".format(hipotenusa))
