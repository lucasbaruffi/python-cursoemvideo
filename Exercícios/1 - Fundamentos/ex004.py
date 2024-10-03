# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite Algo: ')

print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético? ',a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Tem apenas letras maiúsculas? ', a.isupper())
print('Tem apenas letras minúsculas? ', a.islower())
print('Está capitalizada? ',a.istitle())