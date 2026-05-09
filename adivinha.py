# Jogo da Adivinhação

from random import randint
computador = randint (0,100)

print ("Seja bem vindo(a) ao jogo da adivinhação !")
print ("Sou seu computador e acabei de pensar em um número entre 0 e 100, tente adivinhar qual é !")

acertou = False
palpites = 0

while not acertou:
    jogador= int (input("Dê seu palpite: "))
    palpites +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print ("Tente um número maior !")
        elif jogador > computador:
            print ("Tente um número menor !")

print ("Parabéns, você acertou o número com {} tentativas !".format(palpites))



 