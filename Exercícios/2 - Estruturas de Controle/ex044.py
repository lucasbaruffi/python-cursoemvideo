# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e a condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista nno cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

v = float(input('Qual o valor do produto? '))
f = input('''Qual a forma de pagamento? 
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual a opção? ''')

if f == '1':
    desc = v*10/100
    print('O valor a ser pago com 10% de desconto é R${:.2f}'.format(v-desc))
elif f == '2':
    desc = v*5/100
    print('O valor a ser pago com 5% de desconto é de R${:.2f}'.format(v-desc))
elif f == '3':
    print('O valor a ser pago é R${:.2f}'.format(v))
elif f == '4':
    pr = int(input('Em quantas parcelas? '))
    acr = v*20/100
    t = v + acr
    print('''O valor a ser pago com juros de 20% é de R${:.2f}
Em {} parcelas de R${}'''.format(t,pr,t/pr))
