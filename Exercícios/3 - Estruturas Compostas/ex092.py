# Crie um programa que leia o nome, ano de nascimento e carteira de 
# trabalho e cadastre-os (com idade) em um dicionário se por acaso a
# CTPS foi diferente de ZERO, o dicionário receberá também o ano de
# contratação. CAlcule e acrescentem aleém da idade, com quantos anos
# a pesso vai se aposentar.
# se aposenta com 35 anos de contribuição
from datetime import date

pessoa = {}
pessoa['nome ']= str(input('Nome: '))
anonasc = int(input('Ano de Nascimento: '))
ano = date.today().year
idade = ano - anonasc
pessoa['idade'] = idade
ctps = int(input('Carteira de Trabalho (0 não tem): '))
pessoa['ctps'] = ctps
if ctps > 0:
    contratação = int(input('Ano de contratação: '))
    pessoa['contratação'] = contratação
    pessoa['salário'] = float(input('Salário: R$'))

    # Aposentadoria:
    tempoTrabalho = ano-contratação
    anosrest = 35 - tempoTrabalho
    idadeaposent = idade + anosrest
    pessoa['aposentadoria'] = idadeaposent

print('=-'*30)

for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')