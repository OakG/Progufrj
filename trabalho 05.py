##########################
##Exercicio 1: Contar o número de palavras no arquivo.
###################################

import fileinput

contador = 0
for s in fileinput.input("Palavras.txt"):
    contador = contador + 1
print "Existem", contador, "palavras no arquivo Palavras.txt\n"


##########################
##Exercicio 2: Maior(es) Palavra(s)
###################################

import fileinput

maiorp = ''  # 'Maior palavra'
maioresp = '' # 'Maiores palavras'

for i in fileinput.input('Palavras.txt'): # Loop para encontrar a maior palavra
    if len(str(i)[0:-1]) > len(maiorp):
           maiorp = str(i)[0:-1]    # NOTA: pequeno corte na string i pois esta possui o charactere
                                    # especial para quebra de linha "\n" em str(i)[-1]

for j in fileinput.input('Palavras.txt'): # Loop para verificar se a maior palavra é unica

    if len(str(j)[0:-1]) == len(maiorp):         # Caso não seja unica, criar uma string concatenando
        maioresp = maiorp + ', ' + str(j)[0:-1]  # todas as palavras com o mesmo tamanho dela

print "As maiores palavras são: " + maioresp + "\n"


## dois for loops no arquivo é desnecessário
## depois concerto o programa.


##########################
##Exercicio 3: Todos os Palindromos do arquivo

###################################

import fileinput

palavras = []
palindromes = []

for i in fileinput.input("Palavras.txt"):
    palavras.append(str(i)[:-1])

for x in range(len(palavras)):
    if str(palavras[x]) == str(palavras[x])[::-1]: # Checa se a string é igual ao seu inverso
        palindromes.append(palavras[x])

print 'As "palavras" palíndromes são:', palindromes, "\n"
# No programa acima, considero possiveis palindromos todas as palavras(linhas)
# contidas no arquivo, inclusive "palavras" de uma só letra, por exemplo.
# Para uma resposta contendo apenas palavras de 3 digitos ou mais,
# a condicional if deveria ser modificada para
#if (str(palavras[x]) == str(palavras[x])[::-1]) and (len(str(palavras[x])) > 2):


##########################
##Exercicio 4: Mostrar palavras com padrão S**V***R**
###################################

import fileinput

palavras = []
resposta = []

for i in fileinput.input("Palavras.txt"):
    palavras.append(str(i)[:-1])

for j in range(len(palavras)):
    if len(palavras[j]) == 10 and str(palavras[j])[0] == 'S' and str(palavras[j])[3] == 'V' and str(palavras[j])[7] == 'R':
        resposta.append(palavras[j])

print "A(s) palavra(s) que corresponde(m) ao padrão S**V***R** é/são:", resposta, "\n"


##########################
##Desafio: Mostrar palavras com padrões escolhidos pelo usuário
###################################

import fileinput
import string
import re

palavras = []
temp = []
resposta = []

for i in fileinput.input("Palavras.txt"):
    palavras.append(str(i)[0:-1])

print "Bem vindo ao buscador de palavras.\nEle funciona com padrões analogos a S**V***R**, onde * é uma letra qualquer.\nUma busca por A*** retornaria palavras começando com A seguido de 3 letras quaisqer"
padrao = raw_input('Digite o padrão que deseja buscar:')

padrao2 = padrao.replace("*", ".") # Pequeno ajuste já que o charactere coringa para expressões
                                   # regulares no Python é "." e não "*".
for j in range(len(palavras)):
    if len(padrao) == len(palavras[j]):
        temp.append(palavras[j])

padrao2 = re.compile(padrao2, re.IGNORECASE)   # transformando o padrão de expressão regular em um
                                               # objeto que não faz distinção entre caixa baixa e alta.

resposta = filter(padrao2.match, temp) # filtra temp (iteravel) com a função (método) .match, da lib re
                                       # .match retorna true se o padrão 'casar' com o objeto sendo iterado
                                       # e filter remove todos os resultados em que a condição (padrao2.match)
                                       # é falsa (i.e qnd .match returna False), para objetos na lista 'temp'

if resposta == []:
    print "Nenhum resultado encontrado."
else:
    print "As palavras que satisfazem o padrão", padrao, "são:", resposta, "\n"
