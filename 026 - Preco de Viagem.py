'''
Desenvolva um programa que pergunte a distância de
uma viagem em Km.Calcule o preço da passagem, cobrando
R$0,50 por Km para viagens de até 200Km e R$0,45 para
viagens mais longas
'''

distancia = float(input("Qual a distância da viagem: "))
if (distancia <= 200):
    preco = distancia * 0.5
    print("Para viagens menores que 200Km!")
    print("O preço da viagem será de: R${:.2f}".format(preco))
else:
    preco = distancia * 0.45
    print("Para viagens maiores que 200Km")
    print("O preço da vaigem será de: R${:.2f}".format(preco))

                    
