# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastr-os em uma lista. Caso o número já exista lá dentro, ele não 
# será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem 
# crescente.

valores = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        continuar = input('Quer continuar: [S/N] ').strip().upper()[0]
        if continuar in 'NS':
            break
    if continuar == 'N':
        break
    
print('=-'*20)

valores.sort()

print('Você digitou os valores ', end='')
for valor in valores:
    print(f'{valor} ', end='')