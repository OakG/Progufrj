##########################
## Exemplo 1: Hello World!
print "Hello World!"



##################################
## Exemplo 2: DRE, notas e média.
dre = input("Digite o numero do aluno: ")
p1 = input("Digite a primeira nota: ")
p2 = input("Digite a segunda nota: ")
p3 = input("Digite a terceira nota: ")
media = (p1+p2*2+p3*2)/5
print "Aluno:", dre
print "Notas:", p1, p2, p3
print "Media:", media
##################################







######################################################
## Exemplo 3: Raizes de equações de segundo grau.
###################################

import math
a, b, c = input('Entre com os coeficientes a, b e c: ')
r1 = 0.0  # raiz 1
r2 = 0.0  # raiz 2
delta = (b**2.0)-(4.0*a*c)
if delta < 0:
    print "A equação não tem raízes reais."
if delta > 0:
    r1 = (-b + math.sqrt(delta))/(2.0*a)
    r2 = (-b - math.sqrt(delta))/(2.0*a)
    print "As raízes são", r1, "e", r2
if delta = 0:
    r1 = -b/2.0*a
    print "A equação possui apenas uma rais real:", r1





################################################
## Exemplo 3: Area e identificação de triangulos
###################################

l1, l2, l3 = input('Forneça os lados do triangulo:')
s = (l1 + l2 + l3)/2.0
equil = False
isos = False
escal = False

if (l1 == l2) or (l1 == l3) or (l2 == l3):
    isos = True
if l1 <> l2 and l2 <> l3:
    escal = True
if (l1 == l2 == l3):
    equil = True
    isos = False

if (l1 > l2+l3) or (l2 > l1+l3) or (l3 > l1+l2):
    print "O triângulo de lados", l1, l2, l3, "não existe"
else:
    area = math.sqrt(s*(s-l1)*(s-l2)*(s-l3))
    print "O triângulo de lados", l1, l2, l3, "tem area", area
if equil:
    print "E é equilátero."
if isos:
    print "E é isóceles."
if escal:
    print "E é escaleno."
