# Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# Quantas pessoas tem mais de 18 anos
# Quantos homens foram cadastrados.
# QUantas mulheres tem menos de 20 anos

maisdezoito = 0
homens = 0
pessoasMais18 = 0
mulheresMenosVinte = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()
    if idade < 20 and sexo == 'F':
        mulheresMenosVinte += 1
    if sexo == 'M':
        homens += 1
    if idade >= 18:
        pessoasMais18 += 1

    print('-'*20)
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break

print('{}FIM DO PROGRAMA{}'.format('='*6,'='*6))
print(f'Total de pessoas com mais de 18 anos: {pessoasMais18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheresMenosVinte} mulheres com menos de 20 anos')
