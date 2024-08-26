
from random import *


jogando = True

score = 0

print('''
Porta da Fortuna!
=========


Existe um super prêmio atrás de uma destas 3 portas!
Advinhe qual é a porta certa para ganhar o prêmio!
     _____    _____    _____
    |     |  |     |  |     |
    | [1] |  | [2] |  | [3] |
    |    o|  |    o|  |    o|
    |_____|  |_____|  |_____| 

''')

while jogando == True:
    print("\nEscolha uma porta (1, 2 ou 3):")
    
    porta_escolhida = int(input())
    portaCerta = randint(1, 3)

    print("A porta escolhida foi a", porta_escolhida)
    print("A porta certa é a", portaCerta)
    if porta_escolhida == portaCerta:
        print("Parabéns!")
        score += 1
    else:
        score = 0
        print("Que peninha!")
    print("Sua pontuação é", score)
    
    print("\nVocê quer jogar de novo? (s/n)")
    resposta = input()
    if resposta == "n":
        jogando = False
print("Obrigado por jogar.")
print("A sua pontuação final é de", score)