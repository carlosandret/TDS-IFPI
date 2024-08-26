from random import *

tentativas =  0

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

while score < 3:
    tentativas += 1 
    print("\nTentativa", tentativas, ": Escolha uma porta (1, 2 ou 3):")
    
    portaEscolhida = int(input())
    
    portaCerta = randint(1, 3)
    print("A porta ecolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)
    
    if portaEscolhida == portaCerta:
        print("Parabéns!")
        score += 1
    else:
        print("Que peninha!")
    print("Sua pontuação atual é", score)
    
print("\n** Você conseguiu! Terminou o jogo em", tentativas, "tentativas **")