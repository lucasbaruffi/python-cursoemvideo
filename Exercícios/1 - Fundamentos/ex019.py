# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome escolhido.

from random import choice

n1 = input('Digite o nome de um aluno: ')
n2 = input('Digite o nome de outro aluno: ')
n3 = input('Digite o nome de outro aluno: ')
n4 = input('Digite o nome de outro aluno: ')

lista = [n1, n2, n3, n4]

escolhido = choice(lista)

print('O alono escolhido foi {}'.format(escolhido))