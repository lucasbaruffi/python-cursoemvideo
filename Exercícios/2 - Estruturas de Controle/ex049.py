# Refaça o desafio 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um
# laço for.

# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n = int(input('Digite um número: '))
for c in range(1,11):
    
    print('{} X {} é igual à {}'.format(c,n,c*n))
