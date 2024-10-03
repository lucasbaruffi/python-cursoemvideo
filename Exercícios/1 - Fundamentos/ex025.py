# Crie um programa que leia o nome deuma pessoa e
# diga se ela tem "SILVA" no nome.

nome = str(input('Digite um nome: '))

nome = nome.upper()

nome = ('SILVA' in nome)

print(nome)