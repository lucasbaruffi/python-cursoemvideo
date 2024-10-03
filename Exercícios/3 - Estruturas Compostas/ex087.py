# Aprimore o desafio anterior, mostrando no final:
# A) a soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha

matriz = [[], [], []] # linhas 1, 2, e 3
pares = 0
terc = 0

for c in range(0,3):
    for cont in range(0,3):
        n = int(input(f'Digite um valor para [{c}, {cont}] ').strip())
        matriz[c].append(n)
        if n % 2 == 0: # Se for par
            pares += n
        if cont == 2: # se for da terceira coluna
            terc += n
print('=-'*20)

for c in range(0,3):
    for cont in range(0,3):
        print(f'[{matriz[c][cont]:^5}]',end='')
    print('')

print('=-'*20)

print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {terc}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')