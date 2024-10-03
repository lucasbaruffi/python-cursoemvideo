# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere: US$1,00 = R$3,24

r = float(input('Quantos reais você tem? '))
d = r/3.24

print('Você pode comprar {:.2f} dólares.'.format(d))