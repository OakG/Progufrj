##############################################
# Exemplo 1 - Tabuada

##############################################

for x in range(3, 21):
    for y in range(1, 21):
        print x, "x", y, "=", x*y


###############################################
# Exemplo 1.1 - Tabuada usando while
##############################################

i = 3
j = 1
while i <= 20:
    while j <= 20:
        print i, "x", j, "=", i*j
        j = j + 1
    j = 1
    i = i + 1


##############################################
# Exemplo 2 - Numeros de Armstrong
##############################################

for i in range(0, 1000):
    centena = i/100
    dezena = (i/10)%10
    unidade = i%10

    if (i == centena**3 + dezena**3 + unidade**3) and (len(str(i)) == 3):
        print i
    i = i + 1


##############################################
# Exemplo 2.2 - Numeros de Armstrong usando while
##############################################

i = 0
while i < 1000:
    centena = i/100
    dezena = (i/10)%10
    unidade = i%10
    if (len(str(i)) == 3) and (i == centena**3 + dezena**3 + unidade**3):
        print i
    i = i + 1


##############################################
# Exemplo 3 - Gerador de datas
##############################################

contador = 0
trinta1 = [1, 3, 5, 7, 8, 10, 12] # Lista contendo meses com 31 dias
trinta = [4, 6, 9, 11]            # Meses com 30 dias


for ano in range(2001, 2005):
    for mes in range(1, 13):
        for dia in range(1, 32):

            if mes in trinta1:
                while (dia <= 31):
                    print str(dia)+"/"+str(mes)+"/"+str(ano)
                    contador = contador + 1
                    break

            if mes in trinta:
                while ( dia <= 30):
                    print str(dia)+"/"+str(mes)+"/"+str(ano)
                    contador = contador + 1
                    break

            if (mes == 2) and ( ano % 4 == 0):
                while (dia <= 29):
                    print str(dia)+"/"+str(mes)+"/"+str(ano)
                    contador = contador + 1
                    break

            if (mes == 2) and not ( ano % 4 == 0):
                while (dia <= 28):
                    print str(dia)+"/"+str(mes)+"/"+str(ano)
                    contador = contador + 1
                    break

print "Total de:", contador, "dias"

