# Apromore o DESAFIO 93 para que ele funcione com vários JOgadoes, incluindo
# um sistema de visualização de detalhes de aproveitamento de cada jog.

# Desafio 93:

# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogoy.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols
# feitos durante o campeonato

jogadores = []

while True:
#######< CADASTRO JOGADOR >############################################
    
    print('-'*30)
    jogador = {}
    gols = []
    totgols = 0

    nome = str(input('Nome: ').capitalize())
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    for c in range(0, partidas):
        gol = (int(input(f'Quantos gols na partida {c+1}? ')))
        gols.append(gol)
        totgols += gol

#####################################################################
###### ADICIONANDO JOGADOR NA BIBLIOTECA 'JOGADOR' ##################
        
    jogador['nome'] = nome
    jogador['gols'] = gols
    jogador['totgols'] = totgols

#####################################################################
###### ADICIONANDO JOGADOR NA LISTA DE JOGADORES ####################
    
    jogadores.append(jogador.copy())

#####################################################################
    
    while True:
        continuar = str(input('Quer continuar? [S/N] ').strip().upper()[0])
        if continuar in 'SN':
            break
        print('Por favor, digite um dado válido [S/N]')
    if continuar == 'N':
        break

#######< FIM CADASTRO JOGADOR >######################################

print('-='*30)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-='*30)

###########################################33

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não exista jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]['nome']}:')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)


# [{'nome': 'Lucas', 'partidas': 3, 'totgols': 3, 'gols': [2, 1, 0]}, 
#  {'nome': 'Marcos', 'partidas': 2, 'totgols': 3, 'gols': [3, 0]}]

print('Programa Encerrado.')
