# Refaça o DESAFIO 051, lendo o primeiro termo e a 
# razão de uma PA, mostrando os 10 primeiros termos da 
# progressão usando a estrutura while

t = int(input("Qual o primeiro termo? "))
r = int(input("Qual a razão? "))
x = 0
while x < 10:
    s = t + r * x
    print(s, end=" -> ")
    x += 1
print('ACABOU')