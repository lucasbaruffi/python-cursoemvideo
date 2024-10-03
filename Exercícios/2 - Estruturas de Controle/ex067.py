# Faça um programa que mostre a tabuada de vários números, um de cada
# vez, para cada valor digitado pelo usuário. O programa será interrompido
# quando o número solicitado foi negativo.

while True:
    v = int(input('Quer ver a tabuada de qual valor? '))
    if v <= 0:
        break
    print('-'*20)
    for c in range(1,11):
        print(f'{v} x {c} = {v*c}')
    print('-'*20)
print('-'*20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre! ')
