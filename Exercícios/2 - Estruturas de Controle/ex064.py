# Crie um programa que leia vários números inteiros pelo
# teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a confição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre
# eles (desconsiderando o flag)

soma = 0
flag = 999
n = 0
quantidade = 0

while n != flag:
    n = int(input('Digite um número: '))
    soma += n
    quantidade += 1

print("A soma dos {} números digitados foi {}".format(soma-flag, quantidade-1))