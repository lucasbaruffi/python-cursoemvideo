# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
an = float(input('Digite um ângulo: '))
a = math.radians(an)

seno = math.sin(a)
cosseno = math.cos(a)
tangente = math.tan(a)

print('seno: {:.3f}\ncosseno: {:.3f}\ntangente: {:.3f}'.format(seno, cosseno, tangente))

