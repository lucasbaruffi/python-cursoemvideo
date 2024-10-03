# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite um nome: '))

nome = nome.split()

pos_ul = len(nome)
primeiro_nome = nome[0]

ultimo_nome = nome[pos_ul-1]

print(primeiro_nome)

print(ultimo_nome)
