# Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos. O programa deve
# perguntar ao usuário se ele quer ou não continuar a digitar valores.

maiorValor = 0
continuar = "S"
soma = 0
quantidade = 0

while continuar == "S":
    n = int(input('Digite um valor: '))
    quantidade += 1
    
    if quantidade == 1:
        menorValor = n

    if n > maiorValor:
        maiorValor = n

    if n < menorValor:
        menorValor = n

    soma += n



    continuar = input("Deseja continuar? [S/N] ").strip().upper()

print('O menor valor foi {} e o maior foi {}'.format(menorValor, maiorValor))
print('Foram digitados {} números cuja soma é {} e a média é {:.2f}'.format(quantidade, soma, soma/quantidade))