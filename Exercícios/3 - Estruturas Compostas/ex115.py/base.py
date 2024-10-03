def linha():
    print('-'*40)

def leiaInt(msg):
    while True:
        try:
            v = int(input(msg))
        except KeyboardInterrupt:
            print('\nO usuário preferiu finalizar o programa.')
            return 'out'
        except:
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
        else:
            return v
    
def leiaFloat(msg):
    while True:
        try:
            v = float(input(msg))
        except KeyboardInterrupt:
            print('\nO usuário preferiu finalizar o programa.')
            return 'out'
        except: 
            print('\033[31mERRO! Digite um número real válido\033[m')
        else:
            return v

def titulo(msg):
    linha()
    print(f'{msg:^40}')
    linha()

def menu():
    titulo('MENU PRINCIPAL')
    print('\033[33m1 -\033[34m Ver pessoa cadastrada\033[m')
    print('\033[33m2 -\033[34m Cadastrar nova Pessoa\033[m')
    print('\033[33m3 -\033[34m Sair do sistema\033[m')
    linha()

    while True:
        opção = leiaInt('\033[33mSua opção: \033[m')

        if opção == 1:
            verPessoas()
            break
        elif opção == 2:
            cadastro()
            break
        elif opção == 3 or opção == 'out':
            sair()
            break
        else:
            print('\033[31mOps! Parece que o valor digitado não está entre as opções\033[m')

def verPessoas():
    from time import sleep
    titulo('PESSOAS CADASTRADAS')
    caminho_arquivo = "C:/Users/lucas/OneDrive/Documentos/Cursos/Python/3 - Estruturas Compostas/ex115.py/pessoas.txt"
    arquivo = open(caminho_arquivo)
    cont = 0
    for linha in arquivo:
        if cont != 0:
            linha.split(',')
            nome, idade = linha.split(',')
            nome = str(nome)
            idade = int(idade)
            print(f'{nome:<25}{f'{idade:>8} anos'}')
            cont += 1
        cont += 1

    if cont == 1:
        print(f'{'~Sem pessoas cadastradas~':^40}')    
    sleep(3)
    menu()

def cadastro():
    from time import sleep
    titulo('NOVO CADASTRO')
    nome = str(input('Nome: ').strip().title())
    idade = leiaInt('Idade: ')

    caminho_arquivo = "C:/Users/lucas/OneDrive/Documentos/Cursos/Python/3 - Estruturas Compostas/ex115.py/pessoas.txt"
    arquivo = open(caminho_arquivo, 'a')

    dados = f'{nome},{idade}'
    arquivo.write('\n' + dados)
    arquivo.close()
    sleep(0.5)
    print(f'Novo registro de {nome} adicionado.')
    sleep(2)
    menu()

def sair():
    from time import sleep
    print('Saindo',end='', flush=True)
    sleep(0.5)
    print('.',end='', flush=True)
    sleep(0.5)
    print('.',end='', flush=True)
    sleep(0.5)
    print('.', flush=True)
    sleep(0.5)
    titulo('FIM DO PROGRAMA')