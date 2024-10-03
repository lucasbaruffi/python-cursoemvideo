# Faça um mini sistema que utiliza o Interactive Help do Python. O 
# usuário vai digitar o comando e o manual vai aparecer. Quando o 
# usuário digitar 'FIM' o programa se encerrará.
# OBS: use cores

def escrevaTítulo(palavra):
    tamanho = len(palavra) + 4
    print('\033[33m~'*tamanho)
    print(f'  {palavra}')
    print('\033[33m~\033[m'*tamanho)


def ajuda():
    escrevaTítulo('SISTEMA DE AJUDA PYTHON')
    
    while True:
        func = input('Função ou Biblioteca > ').lower().strip()
        print(f'\033[31m{help(func)}\033[m')



        if func == 'fim':
            break



ajuda()