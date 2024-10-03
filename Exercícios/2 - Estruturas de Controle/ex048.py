# Faça um programa que calcule a soma entre todos os
# numeros impares que são multiplos de três e que se
# encontram no intervalo de 1 até 500.
s = 0
cont = 0
for c in range(1, 500, 2):
    # verifica se é multiplo de 3:
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma de todos os {} valores é {}'.format(cont,s))