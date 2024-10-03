# Faça um programa que leia um número qualquer
# e mostre o seu fatorial.
# EX.: 5! = 5x4x3x2x1 = 120

# math

from math import factorial
n = int(input('Digite um valor: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n,f))


# While:

x = 1
while n > 0:
    x *= n
    n = n-1
print('Seu fatorial é {}'.format(x))

# For