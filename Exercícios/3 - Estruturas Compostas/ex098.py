# Faça um programa que tenha uma função chamada contador(), que receba
# três parâmetros: inicio, fim e passo e realiza a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 2
# B) De 10 até 0, de 2 em 2 
# C) Uma contagem personalizada.
from time import sleep

def linha():
    print('-='*30)

def contagem(inicio, fim, passo):
    linha()

    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1.5)

    if inicio < fim:
        cont = inicio
        while cont < fim:
            print(f'{cont}', end=' ', flush=True) # Desliga o buffer de tela / congelamento
            sleep(0.5)
            cont += passo

    elif inicio > fim:
        cont = inicio
        while cont > fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= passo

    print('FIM!')


# Programa principal
contagem(1, 10, 1)
contagem(10, 0, 2)

linha()
print('Agora é a sua vez de personalizar a contagem')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)