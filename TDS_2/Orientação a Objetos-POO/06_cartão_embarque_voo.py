# Utilizando o processo de abstração, implemente uma classe em Python que represente um
# cartão de embarque de voo. Identifique atributos mutáveis e imutáveis, implemente um
# construtor da classe e métodos para manipulação dos atributos mutáveis. Faça todas as
# validações possíveis. Crie objetos para testar os métodos implementados.

from random import *

def assentos_do_voo():
    return randint(10, 111)

class Cartao_embarque:
    def __init__(self, nome_passageiro, numero_voo, codigo_reserva, data, hora, status_checkin = 'Não realizado', num_assento = 'Não selecionado'):
        self.nome_passageiro = nome_passageiro
        self.numero_voo = numero_voo
        self.codigo_reserva = codigo_reserva
        self.data = data
        self.hora = hora
        self.status_checkin = status_checkin
        self.num_assento = num_assento
    
    def realiza_checkin(self):
        self.status_checkin = 'Realizado'
        self.num_assento = assentos_do_voo()
        self.assentos = []
        self.assentos.append(self.num_assento)

    def altera_assento(self, n_assento):
        if self.status_checkin == 'Realizado':
            if self.confere_assento_disponivel(n_assento):
                self.num_assento = n_assento
    
    def confere_assento_disponivel(self, n_assento):
        return n_assento not in self.assentos

    def __str__(self):
        s1 = f'Nome passageiro: {self.nome_passageiro}\nNúmero do voo: {self.numero_voo}\nCógigo da reserva: {self.codigo_reserva}'
        s2 = f'\nData e hora de embarque: {self.data} às {self.hora} horas\nStatos do Check-in: {self.status_checkin}\nNúmero assento: {self.num_assento}'
        return s1+s2

def main():
    cartao_1 = Cartao_embarque('Carlos André', 13, 5, '13/01/2024', '12:00')
    cartao_2 = Cartao_embarque('Carlos André', 13, 5, '13/01/2024', '12:00')
    cartao_3 = Cartao_embarque('Carlos André', 13, 5, '13/01/2024', '12:00')
    
    print(cartao_1)

if __name__=='__main__':
    main()