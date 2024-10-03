# Faça um programa que leia ukm ano qualquer e mostre se ele é BISSEXTO.

# ANos divisíveis por quatro, exceto multiplos de 100 q n são multiplos de 400

from datetime import date

ano = int(input("Qual ano quer consultar? Considere 0 como o ano atual "))

if ano == 0:
    ano = date.today().year

if ano % 4  == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} bissexto'.format(ano))
else:
    print("O ano {} é bissexto".format(ano))