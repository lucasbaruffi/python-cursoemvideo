# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))

ant = n-1
sus = n+1

print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}'.format(n,ant,sus))