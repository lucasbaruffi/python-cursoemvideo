# Desenvolva um programa que leia o nome, idade e sexo
# de 4 pessoas. No final do programa, moste:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.



mulheresMenosVinte = 0
idadeGrupo = 0
x = 1
reg_idade = 0
for c in range(1,5):
    print('----- Registro pessoa {} -----'.format(x))
    n = input('Um nome: ').strip()
    i = int(input('A idade: '))
    s = input('''Sexo:
[ 1 ] Masculino
[ 2 ] Feminino
Qual escolhe? ''').strip()
    
    if s == '2': # Se é mulher
        
        if i < 20: # Se é mulher e tem menos de vinte
            mulheresMenosVinte += 1

    if s == '1': # Se é homem
        if i > reg_idade: # Se é o homem mais velho
            nomeMaisVelho = n
            reg_idade = i
            idade_homem_mais_veho = i
    x += 1
    idadeGrupo += i

print('A média de idade do grupo é {} anos'.format(idadeGrupo/4))
print('O homem mais vélho é o {}, com {} anos'.format(nomeMaisVelho,idade_homem_mais_veho))
print('Há {} mulheres com menos de 20 anos'.format(mulheresMenosVinte))