# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# PAra salários superiores a R$1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

s = float(input('Qual seu salário? '))

if s <= 1250.00:
    aum = s/100*15
    print('Seu salário será de R${:.2f}'.format(s+aum))
else:
    aum = s/100*10
    print('Seu salário será de R${:.2f}'.format(s+aum))