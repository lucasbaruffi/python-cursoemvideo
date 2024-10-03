# Faça um programa que leia nome e peso de várias pessoas, guardando tudo
# em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas;
# B) Uma listagem com as pessoas mais pesadas;
# C) Uma listagem com as pessoas mais leves

galera = []
pessoa = []
mai = men = 0

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(galera) == 0:
        mai = men = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[1]
        if pessoa[1] < men:
            men = pessoa[1]
    galera.append(pessoa[:])
    pessoa.clear()
    while True:
        continuar = input('Quer continuar: [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break

print('-='*30)
print(f'Ao todo, você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in galera:
    if p[1] == mai:
        print(f'{p[0]}' , end='')
print(f'\nO menor peso foi de {men}Kg Peso de ', end='')
for p in galera:
    if p[1] == men:
        print(f'{p[0]}' , end='')