# Reescrevva a função leiaInt() que fizemos no desafio 104, incluindo 
# agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma 
# funcionalidade.

def leiaInt():
    while True:
        try:
            v = int(input('Digite um Inteiro: '))
        except KeyboardInterrupt:
            print('\nO usuário preferiu finalizar o programa.')
            return 0
        except:
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
        else:
            return v
    

def leiaFloat():
    while True:
        try:
            v = float(input('Digite um Real: '))
        except KeyboardInterrupt:
            print('\nO usuário preferiu finalizar o programa.')
            return 0
        except: 
            print('\033[31mERRO! Digite um número real válido\033[m')
        else:
            return v


# Programa principal
i = leiaInt()
r = leiaFloat()
print(f'O valor inteiro digitado foi {i} e o real foi {r:.2f}')
