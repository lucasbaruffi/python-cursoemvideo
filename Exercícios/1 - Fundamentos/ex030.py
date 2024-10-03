# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número: '))

n = n%2

if n == 0:
    print('O número é \033[34mPAR\033[m')
else:
    print('O número é \033[34mIMPAR\033[m')