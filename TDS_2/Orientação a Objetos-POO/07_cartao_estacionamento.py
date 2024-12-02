import datetime
from random import randint, choice

class Cartao_estacionamento:
    def __init__(self, status_cartao = 'Ativo'):
        self.numero_cartao = self.gera_numero_cartao()
        self.data_entrada, self.hora_entrada = 0, 0
        self.status_cartao = status_cartao
        self.valor_total = 0

    def gera_numero_cartao(self):
        alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        letras = []
        for c in range(3):
            c = choice(list(alfabeto))
            letras.append(c)
        numeros = []
        for c in range(5):
            c = randint(0, 10)
            numeros.append(str(c))
        return f'{''.join(letras)}{''.join(numeros)}'
    
    def data_e_hora_entrada(self):
        pass
    
    def registra_saida(self):
        pass

    def consultar_valor_acumulado(self):
        pass

    def 


def main():
    meu_cartao = Cartao_estacionamento()
    print(meu_cartao.numero_cartao)

main()