'''
Crie um programa que leia dois valores e mostre
um menu como o ao lado na tela:
Seu programa deverá realizar a operação solicitada
em cada caso.
[1] - somar
[2] - multiplicar
[3] - maior
[4] - novos numeros
[5] - sair do programa
'''

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))
opcao = 0
while opcao != 5:
    print("""
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos Numeros
    [5] - Sair do Programa
    """)
    opcao = int(input("Informe uma opção:"))

    if opcao == 1:
        soma = num1 + num2
        print("{} + {} = {}".format(num1,num2,soma))
    elif opcao == 2:
        multiplica = num1 * num2
        print("{} * {} = {}".format(num1,num2,multiplica))
    elif opcao == 3:
        if num1 > num2:
            print("O número {} é maior que o número {}!".format(num1,num2))
        else:
            print("O número {} é maior que o número {}!".format(num2,num1))
    elif opcao == 4:
        numeroNovo = int(input("Informe um número novo: "))
        numeroNovo1 = int(input("Informe um outro número novo:"))
    elif opcao == 5:
        print("Você saiu do programa!")
    else:
        print("Opção Inválida!!!")
