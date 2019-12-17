'''Escreva um programa que leia um valor
em metros e o exiba convertido em centimetros
e milimetros'''

medida = int(input("Informe uma medida:"))
print("A medida de {}m convertida é:".format(medida))
conversao1 = medida/1000
conversao2 = medida/100
conversao3 = medida/10
conversao4 = medida*10
conversao5 = medida*100
conversao6 = medida*1000
print("{}m para km é {}km".format(medida,conversao1))
print("{}m para hm é {}hm".format(medida,conversao2))
print("{}m para da é {}dam".format(medida,conversao3))
print("{}m para dm é {}dm".format(medida,conversao4))
print("{}m para cm é {}cm".format(medida, conversao5))
print("{}m para mm é {}mm".format(medida, conversao6))
