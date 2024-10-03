# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade,:
# - Se ele ainda vai se alistar ao serviço militar;
# - Se é a hora de se alistar;
# = Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou passou do prazo.
from datetime import date

print('''Qual seu sexo?
[ 1 ] Masculino
[ 2 ] Feminino''')
sex = int(input('Qual escolhe? '))

if sex == 1:

    ano = int(input('Você nasceu em que ano? '))

    ano_atual = date.today().year

    idade = ano_atual-ano

    if idade == 18:
        print('Está na hora de se alistar, você tem {} anos'.format(idade))
    elif idade > 18:
        print('Já passou do tempo de se alistar;')
        print('Você está {} ano(s) atrasado.'.format(idade-18))
    else:
        print('Faltam {} anos para você se alistar'.format(18-idade))

elif sex == 2:
    print('Você não precisa se alistar, ufa!')

else:
    print('Não entendi qual opção escolheu')

