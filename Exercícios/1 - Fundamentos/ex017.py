# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente deum triângulo retângulo, calcule e mostre o 
# Comprimento da hipotenusa

import math

co = float(input('Tamanho do cateto oposto: '))
ca = float(input('Tamanho do cateto adjascente: '))

h = math.sqrt((co**2)+(ca**2))

print('O tamanho da hipotenusa é {:.2f}'.format(h))

# ou

hi = math.hypot(co,ca)

print('O tamanho da hipotenusa é {:.2f}'.format(hi))

# Resolvido