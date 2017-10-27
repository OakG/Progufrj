##############################################
# Exemplo 1 - Lançador de dados
##############################################
import random
faces = 6  # Numero de lados do dado
print "Simulador de lançamento de dados de", faces, "lados"
print "Primeira jogada:", random.randint(1, faces)

while (True): # Este loop é a resposta para o desafio 1.1
    jogar = input("Gostaria de jogar o dado novamente? Entre 1 para sim e 0 para não: ")
    while (jogar <> 0) and (jogar <> 1):
        jogar = input("Input inválido. Forneça 1 para sim ou 0 para não: ")
    if (jogar == 1):
        print "O novo resultado é:", random.randint(1, faces)
    if (jogar == 0):
        print "Fim de jogo!"
        break

# Com relação ao desafio 1.2: "Como ficaria o programa se o
# seu dado tivesse uma quantidade de faces diferente de 6?"
# RESP: Bastaria modificar a integral faces (linha 7) para o numero de lados desejado.

##############################################
# Exemplo 2 - Advinhação
##############################################
import random
x = random.randint(0, 49)
y = random.randint(50, 99)
score = 0
resul = random.randint(x, y)
while (True):
    print "Advinhe o numero sorteado entre", x, "e", y
    palpite = input("Seu palpite? ")
    if (palpite < resul):
        print "Escolha um numero maior."
    if (palpite > resul):
        print "Escolha um numero menor."
    if (palpite < 0 or palpite > 99):
        print "Escolha ao menos um numero dentro do intervalo, tolo!"
    if (palpite == resul):
        score = score + 1
        x = random.randint(0, 49)
        y = random.randint(50, 99)
        resul = random.randint(x, y)
        print "Parabéns, vocẽ acertou!"
        if (score == 1):
            print "Até agora você acertou", score, "vez"
        else:
            print "Até agora você acertou", score, "vezes"
