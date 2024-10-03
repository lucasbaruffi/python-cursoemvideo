# Faça um programa que tenha uma função chamada ficha(), que receba dois 
# parâmetros opcionais: o nome de um jogador e quantos gols ele marcou

# O progama deverá ser capaz de mostrar a ficha do jogador, mesmo que 
# algum dado não tenha sido informado corretamente

def ficha(n=0, g=0):
    if not n:
        n = '<desconhecido>'
    if not g:
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


# Programa principal
print('-'*20)
nome = str(input('Nome do Jogador: '))
gols = str(input('Número de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(nome, gols)