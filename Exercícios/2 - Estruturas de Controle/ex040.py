# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5: REPROVADO
# - Média entre 5 e 6.9: RECUPERAÇÂO
# - Média 7 ousuperior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2

if m < 5.0:
    print('REPROVADO, sua média foi {}'.format(m))
elif m > 5.0 and m <= 6.9:
    print('RECUPERAÇÂO, sua média foi {}'.format(m))
else:
    print('APROVADO, sua média foi {}'.format(m))
