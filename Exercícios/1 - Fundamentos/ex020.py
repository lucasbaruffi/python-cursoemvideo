# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. faça um programa que leia o nome
# dos quatro alunos e motre a ordem sorteada.

from random import shuffle
n1 = input('Digite o nome de um aluno: ')
n2 = input('Digite o nome de outro aluno: ')
n3 = input('Digite o nome de outro aluno: ')
n4 = input('Digite o nome de outro aluno: ')

lista = [n1, n2, n3, n4]

shuffle(lista)

print('A ordem de apresentação será ')
print(lista)