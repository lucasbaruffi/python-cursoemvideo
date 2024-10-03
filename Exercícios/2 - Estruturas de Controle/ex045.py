# Crie um programa que faça o cimputador jogar Jokenpõ com vc
from random import choice

lista = ['pedra', 'papel', 'tesoura']

p1 = choice(lista)

print('### VAMOS JOGAR JOKENPÔ?###')
p2 = input("Escolha entre: Pedra, Papel e Tesoura: ")

p2 = p2.lower()
p2 = p2.strip()

if p1 == 'pedra' and p2 == 'papel' or p1 == 'papel' and p2 == 'tesoura' or p1 == 'tesoura' and p2 == 'pedra':
    print('Você venceu!!')
elif p1 == p2:
    print('Empate')
else:
    print('Você perdeu!!')

print('Eu escolhi {}'.format(p2))