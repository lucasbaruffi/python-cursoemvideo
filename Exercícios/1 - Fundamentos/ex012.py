# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Preço do produto: '))

d = p-(p*5/100)

print('Se o produto custa R${:.2f}, com o desconto de 5% ele fica por R${:.2f}.'.format(p,d))