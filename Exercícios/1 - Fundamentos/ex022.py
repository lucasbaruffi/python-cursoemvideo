# Crie um programa que leia o nome completo de uma pessoa e mostre:

nome = str(input('Seu nome completo: '))

# O nome com todas as letras maiúsculas
maiusc = nome.upper()
print(maiusc)

# O nome com todas as letras minúsculas
minusc = nome.lower()
print(minusc)

# Quantas letras ao todo (sem considerar espaços)
SemEspaco = len(nome.replace(' ',''))
print(SemEspaco)


# Quantas letras tem o primeiro nome:
div = nome.split()
print(len(div[0]))

