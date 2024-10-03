# Crie um programa que leia o ano de nascimento de 
# sete pessoas. No final, mostre quantas pessoas 
# ainda não atingiram a maioridade e quantas já
# são maiores.

from datetime import date

ano_atual = date.today().year

maior = 0
menor = 0

for c in range (0,7):
    ano_nasc = int(input('Ano de nascimento: '))
    if ano_atual - ano_nasc <= 21:
        maior += 1
    else:
        menor += 1
print('Há {} pessoas na maioridade'.format(maior))
print('{} pessoas ainda não estão na maioridade'.format(menor))