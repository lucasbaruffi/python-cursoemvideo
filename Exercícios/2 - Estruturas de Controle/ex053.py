# Crie um programa que leia uma frase e diga se ela é
# um palíndromo, desconsiderando os espaçoes.
# Ex:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

f = input('Escreva uma frase: ')

f = f.upper()

f = f.replace(" ", "")

f_invert = f[::-1]

print('O inverso de {} é {}'.format(f,f_invert))

if f == f_invert:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')