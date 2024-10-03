# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do
# Campeonato Brasileiro de Futebol, na ordem de colodação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela
# C) Uma lista com os times em ordem alfabética.
# D) EM que posição na tabela está o time do Vasco.

times = ('Atletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 
         'Botafogo', 'Corinthians', 'Criciúma', 'Cruzeiro', 
         'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 
         'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 
         'Bragantino', 'São Paulo', 'Vasco da Gama', 'EC Vitória')

print(f'Lista de times do Brasileirão: {times}')
print('-='*20)
print(f'Os 5 primeiros colocados são {times[:5]}')
print('-='*20)
print(f'Os 4 últimos times são {times[-4:]}')
print('-='*20)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('-='*20)
print(f'O Vasco está em {times.index('Vasco da Gama')+1}º na colocação')