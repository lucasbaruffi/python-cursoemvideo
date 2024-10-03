# Crie um programa que tenha a função leiaInt(), que vai funcionar
# semelhante à função input() do python, só que fazendo a validação
# para aceitar apenas um valor numérico

def leiaInt(msg):
    while True:
        v = str(input(f'{msg}'))
        if v.isnumeric():
            v = int(v)
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
    return v


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
