# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com 
# valores lidos pelo teclado.
# No final, mostre a matriz com a formatação correta.

matriz = [[], [], []] # linhas 1, 2, e 3

for c in range(0,3):
    for cont in range(0,3):
        n = int(input(f'Digite um valor para [{c}, {cont}] ').strip())
        matriz[c].append(n)

for c in range(0,3):
    for cont in range(0,3):
        print(f'[{matriz[c][cont]:^5}]',end='')
    print('')