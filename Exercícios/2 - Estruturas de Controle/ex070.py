# Crie um progra a que leia o nome e o preço de vários produtos. O
# programa deverá perguntar se o usuário vai continuar. NO final, mostre:
# Qual é o total gasto na compra
# Quantos produtos custam mais de R$1000
# QUal é o nome do produto mais barato

totalGasto = 0
maisDeMil = 0
valormaisbarato = 0
cont = 0
nomeMaisBarato = ''

print('-'*30)
print('{}LOJA SUPER BARATÃO{}'.format(' '*5, ' '*5))
print('-'*30)

while True:
    nome = input('Nome do Produto: ')
    valor = float(input('Preço: R$'))
    totalGasto += valor
    cont += 1
    if cont == 1:
        valormaisbarato = valor
        nomeMaisBarato = nome
    elif valor < valormaisbarato:
        valormaisbarato = valor
        nomeMaisBarato = nome

    if valor > 1000:
        maisDeMil +=1
    
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar: [S/N] ').upper().strip()[0]
    if resp == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'''O total da compra foi R${totalGasto:.2f}
Temos {maisDeMil} produtos custando mais de R$1000.00
O produto mais barato foi {nomeMaisBarato} que custa R${valormaisbarato:.2f}''')