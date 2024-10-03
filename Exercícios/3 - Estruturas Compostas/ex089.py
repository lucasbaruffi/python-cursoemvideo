# Crie um programa que leia nome e duas notas de vários alunos e guarde
# tudo em uma lista composta. No final, mostre um boletim contendo
# a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente
# [[aluno[notas]][aluno[notas]][aluno[notas]]]

from time import sleep

turma = []
aluno = []
notas = []
número = []
contador = 0

while True:
    aluno.append(contador)
    aluno.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas[:]) 
    turma.append(aluno[:])
    aluno.clear()
    notas.clear()

    contador += 1
    while True:
        cont = input('Quer continuar? [S/N] ').upper().strip()[0]
        if cont in 'SN':
            break
    if cont == 'N':
        break

print('-='*30)
print(f'{'N°':<4}{'NOME:':<10}{'MÉDIA':>8}')
print('-'*30)

for c, aluno in enumerate(turma):
    número = turma[c][0]
    nome = turma[c][1]
    média = ((turma[c][2][0])+(turma[c][2][1]))/2
    print(f'{número:<4}{nome:<10}{média:>8.2f}')

while True:
    print('-'*30)
    while True:
        a = int(input('Mostrar notas de qual aluno? (999 iterrompe): '))
        if a == 999:
            break        
        elif a > len(turma)-1:
            print('Digite um valor correto. ')
        else:
            print(f'As notas de {turma[a][1]} são {turma[a][2]}')    
    break
print('Finalizando...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')