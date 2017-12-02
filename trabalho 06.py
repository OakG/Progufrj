#########################################
## Exercicio 1. Criptografia simples
###################################
import string
alfabeto = string.ascii_uppercase
cripto = ""
msg = "QUALQUER BOBAGEM"
for i in range(len(msg)):
    if msg[i] in alfabeto:
        pos = alfabeto.index(msg[i])
        letra = alfabeto[(pos+3)%len(alfabeto)] ## Variaçao da cifra de césar
        cripto = cripto + letra                 ## 'rotação' +3
    else:
        cripto = cripto + msg[i]
print cripto + "\n"


##########################################
## Exercício 2. Criptografia com chaves
###################################
chave1 = "ZENIT"
chave2 = "POLAR"
msg = "TESTE DE ACIDEZ"
cripto = ''
for i in range(len(msg)):
    if msg[i] in chave1:
        pos = chave1.index(msg[i])
        letra = chave2[pos]
        cripto = cripto + letra
    else:
        cripto = cripto + msg[i]
print cripto + "\n"


##########################################
## Exercicio 3: Ler um .txt e codificar cada linha.
## Desafio: Escrever as msgs codificadas em um .txt
###################################
import fileinput
import string

def Criptografa(msg):  # Aplica variação (de rotação 3) da cifra de césar em uma string.
    alfabeto = string.ascii_uppercase
    cripto = ""

    for i in range(len(msg)):
        if msg[i] in alfabeto:
            pos = alfabeto.index(msg[i])
            letra = alfabeto[(pos+3)%len(alfabeto)]
            cripto = cripto + letra
        else:
            cripto = cripto + msg[i]
    return cripto
print "Original = QUALQUER BOBAGEM\nCriptografada = "+Criptografa("QUALQUER BOBAGEM")
mcripto = [] # 'mensagens criptografadas'
for i in fileinput.input('aux/entrada.txt'): 
    mcripto.append(Criptografa(str(i)[0:-1]))
#stringsaida = ''
#for j in range(len(mcripto)):
#    strsaida = strsaida + mcripto[j] + "\n"
strsaida = '\n'.join(mcripto)+'\n'
print 'As mensagens criptografadas do arquivo "entrada.txt" são:'
print strsaida


###Desafio: Salvando as msgs criptogradas num arquivo:
saida = open('saida.txt', 'w')
saida.write(strsaida)
saida.close()
print "E estas foram salvas no arquivo saida.txt"
