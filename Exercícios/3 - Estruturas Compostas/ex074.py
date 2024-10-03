# Crie um programa que vai gerar 5 números aleatórios e colocar em uma
# tupla. Depois dissom, moestre a listagem de números gerados e também 
# indique o menor e o maior valor que estão na tupla.

import random
lista = (
random.randint(1,10),
random.randint(1,10),
random.randint(1,10),
random.randint(1,10),
random.randint(1,10),
)

lista_em_ordem = sorted(lista)

print('Os valores sorteados foram: ', end='')
for n in lista:
    print(f'{n} ', end='')

print(f'\nO maior valor sorteado foi {lista_em_ordem[-1]}')
# ou max e min
print(f'O menor valor sorteado foi {lista_em_ordem[0]}')