from random import *

def escolhe_vencedor(e1, e2):
    if e1 == 1 and e2 == 2:
        resultado = 'Você venceu!!'
    elif e1 == 2 and e2 == 3:
        resultado = 'Você venceu!!'
    elif e1 == 3 and e2 == 1:
        resultado = 'Você venceu!!'
    elif e1 == 2 and e2 == 1:
        resultado = '{hone} venceu!!'
    elif e1 == 2 and e2 == 3:
        resultado = 'Você venceu!!'
    elif e1 == 3 and e2 == 1:
        resultado = 'Você venceu!!'

def main():
    while True:
        print("," + '-'*8 +' JOGO DA VELHA ' + '-'*8 + ',' )
        escolha_usuario = input('''Escolha uma das opções:
    [ 1 ] PAPEL
    [ 2 ] PEDRA
    [ 3 ] TESOURA
    [ q ] Fehar jogo
    --> ''')

        escolha_computador = randint(1, 3)
        print(escolha_computador)

        if escolha_computador == 'q': break

if __name__== "__main__":
    main()