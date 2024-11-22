# Utilizando o processo de abstração, implemente uma classe em Python que represente um
# cartão de embarque de voo. Identifique atributos mutáveis e imutáveis, implemente um
# construtor da classe e métodos para manipulação dos atributos mutáveis. Faça todas as
# validações possíveis. Crie objetos para testar os métodos implementados.
from random import *

def assentos_do_voo():
    assentos = []
    for c in range(5):
        assentos.append(randint(1, 100))
    return assentos
    
class Cartao_embarque:
    def __init__(self, nome_passageiro, numero_voo, codigo_reserva, data, hora, status_checkin = 'Não realizado', num_assento = 'Não selecionado'):
        self.nome_passageiro = nome_passageiro
        self.numero_voo = numero_voo
        self.codigo_reserva = codigo_reserva
        self.data = data
        self.hora = hora
        self.status_checkin = status_checkin
        self.num_assento = num_assento
        self.assentos = assentos_do_voo()
    
    def realiza_checkin(self):
            self.status_checkin = 'Realizado'
            self.num_assento = choice(self.assentos)

    #Função para alterar o assento do passageiro
    def altera_assento(self, n_assento):
        if self.status_checkin == 'Realizado':
            #confere se o assento está disponível antes de adicionar
            try: 
                self.confere_assento_disponivel(n_assento)
                self.num_assento = n_assento
            except ValueError:
                print('Erro: este assento não está disponível')
        else:
            return 'Realize o check-in antes de trocar de assento'
    
    def confere_assento_disponivel(self, n_assento):
        return n_assento in self.assentos
    
    def certifica_apenas_um_checkin(self):
        if self.status_checkin == 'Realizado':
            pass

    def __str__(self):
        s1 = f'Nome passageiro: {self.nome_passageiro}\nNúmero do voo: {self.numero_voo}\nCógigo da reserva: {self.codigo_reserva}'
        s2 = f'\nData e hora de embarque: {self.data} às {self.hora} horas\nStatos do Check-in: {self.status_checkin}\nNúmero assento: {self.num_assento}'
        return s1+s2

def menu_cartao_embarque(nome_passageiro, numero_voo, cod_reserva, data, hora):
    meu_cartao_embarque = Cartao_embarque(nome_passageiro, numero_voo, cod_reserva, data, hora)
    print(meu_cartao_embarque)
    while True:
        opcao = int(input('''\nEscolha uma opção:
    [ 1 ] Realizar check-in
    [ 2 ] Alterar assento
    [ 3 ] Terminar
    --> '''))
    
        if opcao == 1:
            meu_cartao_embarque.realiza_checkin()
            print(meu_cartao_embarque)
        elif opcao == 2:
            assento = int(input(f'Escolha o novo assento: {meu_cartao_embarque.assentos} '))
            meu_cartao_embarque.altera_assento(assento)
            print(meu_cartao_embarque)
        elif opcao == 3:
            break
        else: print('Escolha uma opção válida!')

    return meu_cartao_embarque   
    
def main():
    cartao_1 = menu_cartao_embarque('Carlos André', 13, 'DEV202', '13/01/2024', '12:00')
    cartao_2 = menu_cartao_embarque('Julia', 15, 'ABC123', '02/05/2024', '20:00')
    cartao_3 = menu_cartao_embarque('João', 20, 'DEF456', '5/08/2024', '17:00')
    
    print('======== Relatório de cartões de embarque ========\n')
    print(cartao_1 + '\n')
    print(cartao_2+ '\n')
    print(cartao_3+ '\n')

if __name__=='__main__':
    main()
