# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

valores = (
int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite o último número número: '))
)

posição_três = -1
n_pares = 0

for pos, n in enumerate(valores):
    if posição_três == -1:
        if n == 3:
            posição_três = pos


print('=-'*15)
# A:
if valores.count(9) != 0:
    if valores.count(9) == 1:
        print('O valor 9 apareceu uma vez')
    else:
        print(f'O valor 9 apareceu {valores.count(9)} vezes')
else:
    print('O valor 9 não foi digitado')

# B:
if posição_três != -1:    
    print(f'O valor 3 apareceu na {posição_três+1}ª posição.')
else:
    print('O valor 3 não foi digitado')

# C:
for n in valores:
    if n % 2 == 0:
        n_pares +=1
        if n_pares == 1:
            print('Os valores pares digitados foram: ', end='')
        print(f'{n} ', end='')

if n_pares == 0:
    print('Não foram digitados números pares')