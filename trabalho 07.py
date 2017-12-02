##########################
##Exercicio 1: Número de ocorrências de cada dezena da MegaSena
### +Desafio 2: Criar .CSV contendo essas ocorrrências
###################################
# NOTA: Achei pertinente resolver o desafio 2 no mesmo programa que o exercicio 1.
#       O desafio 1 está separado num programa próprio, mais abaixo
import fileinput
import string
strsaida = ''  # placeholder para string de saida (output) do desafio 2
for dez in range(1, 61):
    contador = 0

    for sorteio in fileinput.input('aux/mega.csv'):  # NOTA: o arquivo 'mega.csv' está formatado contendo apenas as
                                                     # 6 dezenas ganhadoras por linha, separadas por ponto-virgulas.

        sorteio = sorteio.strip() # Remove char quebra de linha "\n" no fim de str(sorteio)
        ldez = sorteio.split(';') # Cria uma lista contendo cada dezena do sorteio

        if str(dez) in ldez: # Checa se a str da dezena está dentro da lista
            contador += 1

    strsaida = strsaida + str(dez) + ";" + str(contador) + "\n" # construindo a string de saida (output) do desafio 2
    print dez, contador

saida = open('ocorrencias.csv', 'w')                   # \
saida.write(strsaida)                                   # \  Desafio 2
saida.close()                                           # /
print "Arquivo 'ocorrencias.csv' salvo com sucesso.\n" # /

##########################
##Desafio 1: Sorte no passado
###################################
import fileinput
import string

print "Tente sua sorte no passado!"
print "Quantas vezes você ganharia se tivesse jogado em TODOS os sorteios da MegaSena, com as mesmas dezenas.\n"
invalido = True

while invalido:
    d1, d2, d3, d4, d5, d6 = input("Entre as 6 dezenas, separadas por virgulas. As dezenas também devem ser distintas:")
    if d1 == d2 or d1 == d3 or d1 == d4 or d1 == d5 or d1 == d6 \
                or d2 == d3 or d2 == d4 or d2 == d5 or d2 == d6 \
                or d3 == d4 or d3 == d5 or d3 == d6             \
                or d4 == d5 or d4 == d6                         \
                or d5 == d6:
        print "As dezenas devem ser distintas!"
        invalido = True
    else:
        invalido = False

quadras = 0
quinas = 0
senas = 0
for sorteio in fileinput.input('aux/mega.csv'):
        acerto = 0 #acertos individuais (de dezenas)
        sorteio = sorteio.strip()
        ldez = sorteio.split(';')

        if str(d1) in ldez:
                acerto = acerto + 1
        if str(d2) in ldez:
                acerto = acerto + 1
        if str(d3) in ldez:
                acerto = acerto + 1
        if str(d4) in ldez:
                acerto = acerto + 1
        if str(d5) in ldez:
                acerto = acerto + 1
        if str(d6) in ldez:
                acerto = acerto + 1

        if acerto == 4 and acerto < 5:
                quadras = quadras + 1
        if acerto == 5 and acerto < 6:
                quinas = quinas + 1
        if acerto == 6:
                senas = senas + 1
print "Com as dezenas:", d1, d2, d3, d4, d5, d6
print "Você teria acertado:\n" + str(quadras) + " Quadras\n" + str(quinas) + " Quinas\n" \
                                                             + "e " + str(senas) + " Megasenas\n"
