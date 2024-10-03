# Faça um programa que leia uma frase e mostre:
# QUantas vezes aparece a letra 'A"
# Em que posição aparece pela primera vez
# Em que posição aparece a ultima vez

frase = str(input('Digite uma frase: '))

frase = frase.upper()

a = frase.count('A')

print('Aparecem {} vezes a letra "A"'.format(a))

pri = frase.find('A')

print('Aparece pela primeira vez na posição {}'.format(pri))

ul = frase.rfind('A')

print('Aparece pela última vez na posição {}'.format(ul))
