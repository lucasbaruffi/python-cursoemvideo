# Crie um programa que leia dois valores e mostre
# um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
# Seu programa deverá realizar a operação solicitada
# em cada caso.

from time import sleep

print('INICIANDO CALCULADORA...')


n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
print('=-='*10)

op = 0

while op != 5:

    op = int(input('''O que você quer fazer?
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa         
Digite aqui: '''))


    # Soma
    if op == 1:
        soma = n1 + n2
        print('=-='*10)
        print('''Você selecionou SOMAR: 
    A soma de {:.2f} e {:.2f} é igual à {:.2f}'''.format(n1,n2,soma))
        print('=-='*10)


    # Multiplicação
    elif op == 2:
        mult = n1*n2
        print('=-='*10)
        print('''Você selecionou MULTIPLICAR: 
    A multiplicação de {:.2f} com {:.2f} é igual à {:.2f}'''.format(n1,n2,mult))
        print('=-='*10)


    # Maior
    elif op == 3:
        print('=-='*10)
        print('Você selecionou MAIOR:')
        print('Você digitou os números {} e {}'.format(n1,n2))
        if n1 > n2:
            print('-> {} é maior que {} <-'.format(n1,n2))
        elif n1 < n2:
            print('-> {} é maior que {} <-'.format(n2,n1))
        else:
            print('Os dois valores são iguais')
        print('=-='*10)

    # Novos números
    elif op == 4:
        print('=-='*10)
        print('Você selecionou Novos Números:')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
        print('=-='*10)

    else:
        print('=-='*10)
        print("Opção inválida, tente novamente")
        print('=-='*10)

    sleep(3)

print('Você encerrou a calculadora')

