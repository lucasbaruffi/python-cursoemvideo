# Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário. No final, coloque
# esse dicionário em ordem, samendo que o vencedor tirou o maior número
# no dado.
from random import randint
from time import sleep
from operator import itemgetter

jogo = {}
ranking = {}

for c in range(0, 4):

    n = randint(1, 6)
    jogo[f'jogador{c+1}'] = n
    
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(f'{'RANKING':-^30}')

for i,v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)