# Faça um programa que tenha uma função notas() que pode receber várias
# notas de alunos e vai retornar um dicionário com as seguintes infos:
# Quantidade de notas
# A maior nota
# A menot nota
# A média da turma
# A situação(opcional) > 7: BOA - 
# Adicione também as docstrings da função.

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :n = uma ou mais notas dos alunos (aceita várias)
    :sit = valor opcional, indicando se deve ou não adicionar a situação
    :return = dicionário com várias informações sobre a situação da turma
    """
    resumo = {}
    resumo['total'] = len(n)
    resumo['maior'] = max(n)
    resumo['menor'] = min(n)
    resumo['média'] = sum(n)/len(n)
    if sit:
        if resumo['média'] < 5:
            situação = 'RUIM'
        elif resumo['média'] < 7:
            situação = 'REGULAR'
        elif resumo['média'] < 10:
            situação = 'BOA'
        else:
            situação = 'ÓTIMA'
        resumo['situação'] = situação
    return resumo


# Programa principal:
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)