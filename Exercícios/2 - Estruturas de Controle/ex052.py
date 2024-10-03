# Faça um programa que leia um número inteiro e diga
# se ele pe ou não um número primo.

n = int(input('Digite um número: '))

if n == 2 or n == 3 or n == 5 or n == 7:
    print('É um número primo')
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print('Não é primo')
else:
    print('É um número primo')