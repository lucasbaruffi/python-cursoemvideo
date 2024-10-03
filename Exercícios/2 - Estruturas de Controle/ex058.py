# Melhore o jogo do desafio 028 onde o computador vai
# pensar em um número entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar
# mostrando no final quantos palpites foram necessários
# para vencer.

# desafio 28:

from random import choice, randint
from time import sleep

print('###### ADIVINHE O NÚMERO ######')

npc = randint(0,10)
n = -1
tentativas = 0
while n != npc:
    n = int(input('Qual número você chuta? '))
    if n == npc:
        print('Você acertou!!!')
        print('Pensei no número {}'.format(npc))
    else:
        if n > npc:
            print('Menos... Tente mais uma vez')
        elif n < npc:
            print('Mais... Tente mais uma vez.')

        tentativas += 1
    
print('O número de tentativas foi: {}'.format(tentativas))
