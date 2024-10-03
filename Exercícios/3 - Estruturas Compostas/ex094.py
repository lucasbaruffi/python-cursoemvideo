# Crie um programa que leia nome, sexo e idade de cárias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os 
# dicionárioe em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas;
# B) A média de idade do grupo;
# C) Uma lista com todas as mulheres;
# D) Uma lista com todas as pessoas com idade acima da média

grupo = []
pessoa = {}
qtd = somaidade = 0
mulheres = []
while True:
    nome = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    idade = int(input('Idade: '))
    pessoa['nome'] = nome
    pessoa['sexo'] = sexo
    pessoa['idade'] = idade
    grupo.append(pessoa.copy())
    qtd += 1
    somaidade += idade
    if sexo == 'F':
        mulheres.append(nome)

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if continuar == 'N':
        break

média = somaidade/qtd
print('=-'*30)
print(f'- O grupo tem {qtd} pessoas.')
print(f'- A média de idade é de {média:.2f} anos.')
print('- As mulheres cadastradas foram: ',end='')
for n in mulheres:
    print(n, end=' ')
print(f'\n- Lista de pessoas que estão acima da média: ')
for p in grupo:
    if p['idade'] > média:
        print(f'{p['nome']}, com {p['idade']} anos')
print('<< ENCERRADO >>')