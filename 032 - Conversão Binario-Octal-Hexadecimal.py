'''
Escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher qual
será a base de conversão:
1 para binario - bin
2 para octal - oct
3 para hexadecimal - hex
'''

print("="*20)
print("      CONVERSÃO")
print("="*20)
numero = int(input("Informe um número para conversão:"))
print("="*25)
print("""Escolha umas das  opções:
    [1] - BINÁRIO:
    [2] - OCTAL:
    [3] - HEXADECIMAL:""")
print("="*25)
opcao = int(input("Informe uma das opções:"))
if opcao == 1:
    print(" O número {} convertido para Binário é:{}".format(numero, bin(numero)))
elif opcao == 2:
    print("O número {} convertido para Octal é: {}".format(numero, oct(numero)))
elif opcao == 3:
    print("O número {} convertido para Hexadecimal é: {}".format(numero, hex(numero)))
else:
    print("Opção Inválida!")
