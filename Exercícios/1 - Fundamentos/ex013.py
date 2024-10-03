# Faça um algorítimo que leia o salário de um funcionário com 15% de aumento

v = float(input('Quanto você ganha? '))

n = v+(v*15/100)

print('Com o aumento de 15%, você passará a ganhar R${:.2f}.'.format(n))