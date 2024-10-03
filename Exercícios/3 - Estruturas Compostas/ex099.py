# Faça um programa que tenha uma função chamada maior(), que receba
# vários parâmetros com valores inteiros.
#Q Seu programa tem que analizar todos os valores e dizer qual deles 
# é o maior
from time import sleep


def maior(*valores):
    print('=-'*20)
    print('Analisando os valores passados...')
    maior = 0
    qtd = 0
    for c, val in enumerate(valores):
        qtd += 1
        print(f'{val} ',end='', flush=True)
        sleep(0.3)
        if c == 0:
            maior = val
        else:
            if val > maior:
                maior = val
    print(f'Foram informados {qtd} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()