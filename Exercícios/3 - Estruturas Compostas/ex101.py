# Crie um programa que tenha uma função chamada voto() que vi receber
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor
# literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou 
# OBRIGATÒRIO nas eleições.
# < 16 negado
# 16 < 17 OPCIONAL
# 18 - 64 OBRIGATÓRIO
# > 65 OPCIONAL

from datetime import date

def voto(idade):
    """
    -> Retorna NEGADO, OPCIONAL ou OBRIGATÓRIO de acordo com a idade 
    < 16 negado
    16 < 17 OPCIONAL
    18 - 64 OBRIGATÓRIO
    > 65 OPCIONAL
    :param a: idade
    :return resultado: retorna se é NEGADO, OPCIONAL ou OBRIGATÓRIO
    """
    if idade < 16:
        resultado = 'NEGADO'
    elif 16 <= idade <= 17:
        resultado = 'OPCIONAL'
    elif 18 <= idade <= 64:
        resultado = 'OBRIGATÓRIO'
    else:
        resultado = 'OPCIONAL'
    return resultado

print('-'*20)
ano = int(input('Em que ano você nasceu? '))
atual
= date.today().year
idade = atual - ano
result =  voto(idade)
print(f'Com {idade} anos: VOTO {result}')