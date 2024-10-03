# FAça um programa que leia nome e média de um aluno, guardando também a 
# situação em um dicionário. No final, mostre o conteúdo da estrutura na tela
# Aprovado >= 7

aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5<= aluno ['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print(f'A média de {aluno['nome']} é {aluno['média']}')
print(f'A situação é {aluno['situação']}')