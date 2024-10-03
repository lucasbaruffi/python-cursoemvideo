# Crie um programa que leia o nome de uma cidade e 
# diga se ela começa ou não com "SANTO"

nome = str(input('Digite o nome de uma cidade: '))

# Maiuscula
nome = nome.upper()

# Sem espaços
nome = nome.strip()

# dividido por palavra
nome = nome.split()

nome = 'SANTO'in nome[0]

print(nome)