# Aula 14

# Faça um programa que leia o sexo de uma pessoa, mas
# só aceite os valores 'M' ou 'F'. Caso esteja
# errado, peça a digitação novamente até ter um 
# valor correto.

sex = str(input('Informe seu sexo: [M/F]  ')).upper().strip()[0]

while sex not in 'MF':
    sex = str(input("Dados inválidos. Por favor, informe seu sexo: ").strip().upper())
print('Sexo {} registrado com sucesso'.format(sex))    
