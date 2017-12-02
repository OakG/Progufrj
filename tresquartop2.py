import random
def XPTO(S):
    lista = list(S)
    lista2 = []
    for letra in lista:
        if letra not in lista2:
            lista2.append(letra)
    return "".join(lista2)


def Beto():
    ALFA = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    alfa = 'abcdefghijklmnopqrstuvxyz'
    CASE = random.randint(0,1)
    if CASE:
        return ALFA[random.randint(0,24)]
    else:
        return alfa[random.randint(0,24)]
# Merda de W.


import fileinput
tam = 0
for S in fileinput.input("aux/Palavras.txt"):
    if len(S) > tam:
        tam = len(S)
print tam
    

