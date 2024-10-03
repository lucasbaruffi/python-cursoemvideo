# Crie um programa onde o usuário digite uma expressão qualquer que use 
# parênteses. Seu aplicativo deverá analizar se a expressão passada está 
# com os parênteses abertos e fechados na ordem correta.

exp = str(input('Digite uma expressão: '))

pilha = []

for letra in exp:
    if letra == '(':
        pilha.append('(')
    elif letra == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão está errada')