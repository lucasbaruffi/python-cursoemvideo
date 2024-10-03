# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogoy.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols
# feitos durante o campeonato
dados = {}
listagols = []

jogador = str(input('Nome do jogador: '))
dados['nome'] = jogador
partidas = int(input(f'Quantas partidas {jogador} jogou? '))
dados['total'] = partidas
partida = 0
while True:
    partida +=1
    listagols.append(int(input(f'Quantos gols na partida {partida}? ')))
    if partida >= partidas:
        break
dados['gols'] = listagols.copy()
print('=-'*30)
print(dados)
print('=-'*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {dados["nome"]} jogou {dados['total']} partidas.')
totgols = 0
for c, e in enumerate(dados['gols']):
    print(f'=> Na partida {c+1}, fez {e} gols.')
    totgols += e
print(f'Foi um total de {totgols} gols')