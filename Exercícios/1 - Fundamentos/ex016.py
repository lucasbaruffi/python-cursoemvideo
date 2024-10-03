# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

n = float(input('Digite um número real: '))
print('A parte inteira do número {} é {}'.format(n,int(n)))

# Ou

from math import trunc

print('A parte inteira do número {} é {}'.format(n,trunc(n)))


# Resolvido