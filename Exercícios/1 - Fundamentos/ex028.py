# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi 
# O programa deverea escrever na tela se o usuário venceu ou peredeu

from random import choice, randint
from time import sleep

lista = [0, 1, 2, 3, 4, 5]

npc = choice(lista)

# ou rendomiza um número inteiro entre 0 e 5

npc = randint(0,5)

n = int(input('Qual número você chuta? '))

print('Processando...')
sleep(2)

if n == npc:
    print('Você acertou!!!')
    print('Pensei no número {}'.format(npc))
else:
    print('Você errou ;-;')
    print('Pensei no número {}'.format(npc))