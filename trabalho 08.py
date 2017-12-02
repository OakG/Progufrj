##
# Exemplo 1: Soma dos 10 primeiro termos
###################################
print "|| EXEMPLO 1 ||"
def SomaInvQuadradosSA(N): # "Soma dos inversos dos quadrados com sinal alternando"
    '''
 Calcula a soma da série dos inversos dos quadrados dos numeros naturais positivos,
 com os sinais dos termos alternando e sendo N o número de termos.
 Se o natural é impar, o sinal do termo é positivo,
 caso contrário, o sinal do termo é negativo.
 Em outras "palavras" a função retorna a seguinte expressão:
 + (1/1**2) - (1/2**2) + (1/3**2) - (1/4**2) + ... +- (1/N**2)
     ^ termo 1                        ^ termo 4         ^ termo N
    '''
    if N <= 0 or type(N) != int:
        return 'Argumento inválido. N deve ser um inteiro maior que 0.'
    Stermosimp = 0.00 # 'Soma dos termos impares'
    Stermospar = 0.00 # 'Soma dos termos pares'
    for i in range(1, N+1):
        if i % 2 != 0:
            Stermosimp += 1.0/(i**2)
        else:
            Stermospar += 1.0/(i**2)
    return Stermosimp - Stermospar
print "A soma dos 10 primeiros termos da série é:"
print 'SomaInvQuadradosSA(10)     = %f' % SomaInvQuadradosSA(10)
print '\n'
print 'SomaInvQuadradosSA(500)    = %f' % SomaInvQuadradosSA(500)
print 'SomaInvQuadradosSA(10000)  = %f' % SomaInvQuadradosSA(10000)
print 'SomaInvQuadradosSA(100000) = %f' % SomaInvQuadradosSA(400000)
print '\n'

##
# Exemplo 2: Aproximação de pi
###################################
import math
def SomaInvQuadradosSA(N):
    if N <= 0 or type(N) != int:
        return 'Argumento inválido. N deve ser um inteiro maior que 0.'
    Stermosimp = 0.00 # 'Soma dos termos impares'
    Stermospar = 0.00 # 'Soma dos termos pares'
    for i in range(1, N+1):
        if i % 2 != 0:
            Stermosimp += 1.0/(i**2)
        else:
            Stermospar += 1.0/(i**2)
    return Stermosimp - Stermospar
    '''
Note que a função:
 (+ 1/1**2 - 1/2**2 + 1/3**2 - 1/4**2 ... +- 1/N**2)
     ^ termo 1                  ^ termo 4     ^ termo N

É extremamente similar ao problema de Basileia
(https://en.wikipedia.org/wiki/Basel_problem)
que buscava o valor exato da soma da seguinte série infinita:
 + 1/1**2 + 1/2**2 + 1/3**2 + 1/4**2 + ... + 1/I**2
(i.e. Soma exata dos inversos dos quadrados de todos numeros naturais positivos)
Este problema é notório e possui resolução conhecida que
descoberta por Euler, resulta em pi**2/6 ou aprox. 1.644934

Ao chamar a função SomaInvQuadradosSA(N) com Ns muito grandes,
pode-se perceber que esta aproxima-se de 0.822467 que,
curiosamente, é (cerca de) metade do resultado do problema de basiléia.
Dessa forma, quando N é grande o suficiente, SomaInvQuadradosSA(N)
tende a metade de pi**2/6.
Chamando x = (pi**2/6)/2 e isolando pi:
2x = pi**2/6 .:. pi**2 = 12*x .:. pi = raiz de (12*x), ou seja:

Quando N é muito grande, raiz de 12*SomaInvQuadradosSA(N) tende a pi.
    '''

print "|| EXEMPLO 2.1 ||"
def AproxPI(N):  # 'Aproximação de pi'
    if N <= 0 or type(N) != int:
        return "Argumento inválido. N deve ser um inteiro maior que 0."
    return math.sqrt(SomaInvQuadradosSA(N)*12)

print "Termos: 10\nValor Calc: AproxPI(10)"
print "AproxPI(10) = %f" %AproxPI(10)
print "\n"


print "|| EXEMPLO 2.2 ||"
passos = [1, 10, 100, 1000, 100000, 1000000]
print "Termos      Val. calculado      Diferenca"
for j in passos:
    aproxpi = AproxPI(j)
    if math.pi > aproxpi:
        difer = math.pi - aproxpi
        print '%i	    %.10f	%.10f' % (j, aproxpi, difer)
    else:
        difer = aproxpi - math.pi
        print '%i	    %.10f	%.10f' % (j, aproxpi, difer)
print '\n'



##
# Exercicio 03: MDC de dois numeros.
###################################
print "|| EXEMPLO 3 ||"
def MDC(a,b):  # Máximo Divisor Comum de a e b, ambos numeros inteiros.
    resp = 1
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a == b and type(a) == int:
        return a
    for i in range(1, min(a,b)+1):
        if a % i == 0:
            if b % i == 0:
                if resp < i:
                    resp = i
    return resp
print "MDC(-4,-16)     = %i" %MDC(-4,-16)
print "MDC(144,153)    = %i" %MDC(144,153)
print "MDC(3247,2944)  = %i" %MDC(3247,2944)
print "MDC(500,-600)   = %i" %MDC(500,-600)
print "MDC(128,1024)   = %i" %MDC(128,1024)
print '\n'

###
# Exemplo 04: Fatorial de N
# Aluno: Marcelo Carvalho Garcia
# DRE: 117251003
###################################
print "|| EXEMPLO 4 ||"
def Fatorial(N):
    # Calcula o valor de N!, sendo N inteiro positvo.
    fat = 1
    if N < 0 or type(N) != int:
        return "Erro. Use um inteiro >= 0."
    if N == 0 or N == 1:
        return fat
    else:
        for i in range(1, N+1):
            fat *= i
        return fat
print "Fatorial(-1)  = " + Fatorial(-1)
print "Fatorial(0)   = %i" % Fatorial(0)
print "Fatorial(21)  = %i" % Fatorial(21)
print "Fatorial(42)  = %i" % Fatorial(42)
print "\n"

#Versão alternativa (recursiva):
def FatorialR(N):
    #Calcula valor de N!, sendo N inteiro positivo.
    if N < 0 or type(N) != int:
        return "Erro. Use um inteiro >= 0."
    else:
        if N == 0 or N == 1:  # Caso(s) base
            return 1
        else:
            return N*FatorialR(N-1)
print "FatorialR(-1)  = " + FatorialR(-1)
print "FatorialR(1.5) = " + FatorialR(1.5)
print "FatorialR(0)   = %i" % FatorialR(0)
print "FatorialR(21)  = %i" % FatorialR(21)
print "FatorialR(42)  = %i" % FatorialR(42)
