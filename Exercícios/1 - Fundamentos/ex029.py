# Faça um programa que leia a velocidade de um carro.
# se ele ultrapassar 80km/h, moestre uma mensagem dizendo que ele foi multado
# a multa vai custar R$7,00 por cada Km acima da média

v = int(input('Qual a velocidade do carro? '))

if v > 80:
    km = v-80
    vlr = float(km*7)
    print('CUIDADO!! VOCÊ FOI MULTADO!!')
    print('A multa será de R${:.2f}.'.format(vlr))

print('Tenha um bom dia! Dirija com segurança')