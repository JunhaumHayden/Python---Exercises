'''
Desenvolva um programa que leia seis números
inteiros e mostre a soma apenas daqueles que
forem pares. Se o valor digitado for impar,
desconsidere-o.
'''
par = 0
for numeros in range(1,7):
    numero = int(input("{}º - Digite um número: ".format(numeros)))
    if numero % 2 == 0:
        par = numero + par
print("A soma dos números PARES é: {}".format(par))
