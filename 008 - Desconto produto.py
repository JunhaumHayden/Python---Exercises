'''Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto'''

print("=============================")
print("           INFORME")
print("=============================")
preco = float(input("Preço do produto: R$"))
print("=============================")
print("O preço do produto atual é: R${}".format(preco))
print()
desconto = preco - (preco*0.05)
print("Com o desconto fica R${}".format(desconto))
