# Desenvolva um programa que leia o primeiro termo e a 
# razão de uma PA. No fina, mostre os 10 primeiros
# termos dessa prograssão

t = int(input("Qual o primeiro termo? "))
r = int(input("Qual a razão? "))
x = 0
for c in range (0,10):
    s = t + r * x
    print(s, end=" -> ")
    x += 1
print('ACABOU')