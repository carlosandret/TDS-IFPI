# Faz a importação da biblioteca random
from random import *

# A variavel determina se o jogador ira continuar jogando
jogando = True
# A variavel recebe a pontuação do jogador
pontuação = 0

print('''Vinte e um!
============
Tente fazer exatamente 21 pontos!''')

# Escolhe um número alatorio 1 a 10
while jogando == True:
    # Escolhe aleatoriamente a quantidade de pontos que será adicionada
    proximo_numero = randint(1, 10)
    pontuação += proximo_numero
    print("\nSeu proximo número é", proximo_numero)
    print("nSua pontuação agora é", pontuação)
    
    # Faz uma pergunta se o usuário deseja continuar ou não
    print("\nGostaria de somar mais um número? (s/n)")
    resposta = input()
    # Faz o encerramento do programa se a resposta for "n"
    if resposta == "n":
        jogando = False

# Mostra a pontuação final e o resultado
print("\nSua pontuação final é", pontuação)
if pontuação == 21:
    print("Você venceu!!".upper())
else:
    print("Que pena!!")
    
    