# Faça um programa que leia um número de 0 a 9999 e 
# mostre na tela cada um dos dígitos separados.
# Ex.:
#1834
# unidade: 4
# dezena: 3
# centena: 8
# minhar: 1

n = str(input('Digite um número de 0 a 9999: '))

# Matematicamente
print('Matematicamente:')

# Ou não
print(' \nPor código')

n = n.zfill(4)

uni = n[3]
dez = n[2]
cen = n[1]
mil = n[0]

print('unidade: {}'.format(uni))
print('dezena: {}'.format(dez))
print('centena: {}'.format(cen))
print('milhar: {}'.format(mil))

# Funciona apenas para maiores de 1000