# Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares
# e ímpares. No final, mostre os valores pares e ímpares em ordem crescente

valores = [[], []]
pares = valores[0]
ímpares = valores[1]

for c in range (0,7):
    v = int(input(f'Digite o {c+1}º valor: '))
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print('-='*20)
pares.sort()
ímpares.sort()
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {ímpares}')
