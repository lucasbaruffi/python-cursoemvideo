# Crie um, programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas

valores = []

while True:
    valores.append(int(input('Digite um número: ')))
    while True:
        cont = input('Quer continuar? [S/N] ').upper().strip()[0]
        if cont in 'SN':
            break
    if cont == 'N':       
        break

print('=-'*20)
pares = []
ímpares = []

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        ímpares.append(valor)

print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')