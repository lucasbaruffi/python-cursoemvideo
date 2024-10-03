# Crie um programa que tenha uma tupla totalmente preenchida com uma 
# contagem por extenso, de zero até vinte.

# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo
# por extenso.

números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: ').strip())
    while n < 0 or n > 20:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: ').strip())
    print(f'Você digitou o número {números[n]}')
    c = input('Você quer continuar? [S/N] ').strip().upper()
    while c not in 'SN':
        c = input('Você quer continuar? [S/N] ').strip().upper()
    if c == 'N':
        break
print('Programa finalizado')