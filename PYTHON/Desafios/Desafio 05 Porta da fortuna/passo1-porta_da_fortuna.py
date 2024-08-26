from random import *

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

for attempt in range(3):
    print("\nEscolha uma porta (1, 2 ou 3):")
    
    porta_escolhida = int(input())
    portaCerta = randint(1, 3)

    print("A porta escolhida foi a", porta_escolhida)
    print("A porta certa é a", portaCerta)
    if porta_escolhida == portaCerta:
        print("Parabéns!")
    else:
        print("Que peninha!")