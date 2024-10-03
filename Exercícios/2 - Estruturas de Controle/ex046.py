# Aula 13:

# Faça um programa que mostre uma contagem regressiva para o estouro de fogos
# de artigicio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print('COMEÇANDO A CONTAGEM!!')

for c in range(10,-1,-1):
    print(c)
    sleep(1)

print('Feliz ano novo!!!')