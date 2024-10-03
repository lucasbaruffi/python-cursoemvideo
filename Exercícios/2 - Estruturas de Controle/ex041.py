# A COnfederaçã nacional de NAtação precisa de um programa que leia o 
# ano de nascimento de um atleta e mostre sua categoria, de acordo 
# com a idade:
# até: 9 anos: MIRIM
# até: 14 anos: INFANTIL
# até: 19 anos: JUNIOR
# até: 20 anos: SENIOR
# acima: MASTER

i = int(input('Qual a idade do atleta? '))

if i <= 9:
    print('MIRIM')
elif i <= 14:
    print('INFANTIL')
elif i <= 19:
    print('JUNIOR')
elif i <= 20:
    print('SÊNIOR')
else:
    print('MASTER')