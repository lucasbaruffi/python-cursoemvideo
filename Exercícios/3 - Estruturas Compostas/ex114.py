# Crie um código que teste se o site Pudim está acessivel pelo 
# computador usado.


import requests

def verifica_disponibilidade(url):
    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            print(f'O site {url} está disponível.')
        else:
            print(f'O site {url} não está disponível. Código de status: {response.status_code}')
    except requests.ConnectionError:
        print(f'O site {url} não pôde ser alcançado.')

# Exemplo de uso
url = 'https://www.pudim.com.br/'
verifica_disponibilidade(url)
