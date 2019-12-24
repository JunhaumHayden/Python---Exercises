'''
Mostre a tabuada de um número que o usuário
escolher, só que agora utilizando um laço for
'''
print("="*15)
print("    TABUADA")
print("="*15)
print()
numero = int(input("Informe um número para a tabuada:"))
print()
for tabuada in range(0,11):
    print("{} x {} = {}".format(numero,tabuada,numero*tabuada))
