# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 quadrados.

v1 = float(input('Qual a largura da sua parede? '))
v2 = float(input('Qual a altura da sua parede? '))

a = v1*v2
l = a/2

print('Sua parede mede {} metros quadrados, você precisa de {} litros de tinta para pintá-la'.format(a,l))