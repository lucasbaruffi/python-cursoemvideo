# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o meior e o menor peso lidos

maior = 0
menor = 9999

for c in range (0,5):
    p = float(input('Qual o peso? '))

    if p > maior:
        maior = p
    elif p < menor:
        menor = p

print('''O maior peso é: {}Kg
O menor é: {}Kg'''.format(maior,menor))

