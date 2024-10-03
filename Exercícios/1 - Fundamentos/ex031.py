# Desenvolva um programa que pergunte a distância de uma viagem em Km. Caucule o preço da passagem, cobrando R$0,50 por KM
# para viagens até 200km e R$0,45 para viagens mais longas

d = float(input('Qual a distância da viagem? '))

if d <= 200.00:
    p = d*0.50
else:
    p = d*0.45

# OU
    
p = d*0.50 if d <= 200 else d*0.45

print('O preço da passagem será de \033[35mR${:.2f}\033[m'.format(p))