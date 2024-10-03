# Faça um programa que jogue par ou ímpar com o computador, o jogo só será iterrompido 
# quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele con
# no final do jogo.
from random import randint
vitórias = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
pi = 'x'
while True:
    v = int(input('Diga um valor: '))
    while pi not in "PI":
        pi = input('Par ou ímpar? [P/I] ').strip().upper()[0]
    npc = randint(0, 5)
    sum = v + npc

    if sum % 2 == 0: # Se o resultado for PAR:
        print('=-'*20)
        print(f'Você jogou {v} e o computador {npc}. Total de {sum} deu PAR')
        print('=-'*20)
        if pi == "P":
            print('''Você VENCEU!
Vamos jogar novamente...''')
            vitórias += 1
        else:
            print('Você PERDEU!')
            break
        print('=-'*20)
    else:
        print('=-'*20)
        print(f'Você jogou {v} e o computador {npc}. Total de {sum} deu IMPAR')
        print('=-'*20)
        if pi == "I":
            print('''Você VENCEU!
Vamos jogar novamente...''')
            vitórias += 1
        else:
            print('Você PERDEU!')
            break
        print('=-'*20)
        
print(f'GAME OVER! Você venceu {vitórias} vezes.')