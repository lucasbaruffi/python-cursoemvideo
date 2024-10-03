# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número
# inteiro) e o programa vai informar quantas cédulas de cada valor 
# Serão entregues
#Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

print('='*30)
print('{:^30}'.format('BANCO BARUFFI'))
print('='*30)

valor = int(input('Qual valor você quer sacar? R$'))

# # Preciso verificar se o valor dividido por R$50 é maior ou igual que 1 para seguir.
# if valor / 50 >= 1:
#     restanteDoValor50 = valor % 50
#     valorDivisível = valor - restanteDoValor50
#     qtdCélulas = valorDivisível / 50
#     print('Total de {} células de R$50'.format(int(qtdCélulas)))
# restanteDoValor50 = valor % 50
# 
# if restanteDoValor50 / 20 >= 1:
#     restanteDoValor = restanteDoValor50 % 20
#     valorDivisível = restanteDoValor50 - restanteDoValor
#     qtdCélulas = valorDivisível / 20
#     print('Total de {} células de R$20'.format(int(qtdCélulas)))
# restanteDoValor20 = restanteDoValor50 % 20
# 
# if restanteDoValor20 / 10 >= 1:
#     restanteDoValor = restanteDoValor20 % 10
#     valorDivisível = restanteDoValor20 - restanteDoValor
#     qtdCélulas = valorDivisível / 10
#     print('Total de {} células de R$10'.format(int(qtdCélulas)))
# restanteDoValor10 = restanteDoValor20 % 10
# 
# if restanteDoValor10 / 1 >= 1:
#     print('Total de {} células de R$1'.format(int(restanteDoValor10)))
# 
# print('='*31)
# print('Volte sempre ao Banco Baruffi, tenha um bom dia!')

# ou:
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao Banco Baruffi, tenha um bom dia!')    