# Faça um programa que ajude um jogador da MEGA SENA a cria palpites. 
# O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
# composta
import random
from time import sleep

jogos = []
jogo = []

print('-'*30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-'*30)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{f' SORTEANDO {qtd} JOGOS ':-^30}')

for c in range(0,qtd):
    cont = 0
    while True:
        n = random.randint(1,60)
        if n not in jogo:
            jogo.append(n)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()     
    jogos.append(jogo[:])
    print(f'Jogo {c+1}: {jogo}')
    jogo.clear()
    sleep(0.7)
print(f'{' < BOA SORTE! > ':-^30}')