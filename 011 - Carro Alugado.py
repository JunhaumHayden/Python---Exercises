'''Escreva um programa que pergunte a quantidade
de Km percorridas por um carro alugado e a quantidade
de dias pelos quais ele foi alugado. Calcule o preço a
pagar, sabendo que o carro custa R$60 por dia e R$0.15
por Km rodado.'''

Km = float(input("Digite a quantidade de Km rodados: "))
dias = int(input("Informe a quantidade de dias: "))
preco = (dias*0.15) + (Km*60)
print("O preço a ser pago pelo carro é: R${}".format(preco))
