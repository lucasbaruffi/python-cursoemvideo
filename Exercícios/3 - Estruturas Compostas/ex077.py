# Crie um programa que tenha uma tupla com várias palavras. Depois disso
#, você deve mostrar para cada palavra, quais são suas vogais

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end="")
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

# finalizado, assitir aula 17