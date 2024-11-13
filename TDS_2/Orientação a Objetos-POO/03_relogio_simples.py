class Relógio_Digital_Simples:
    def __init__(self, hora, minuto):
        self.horas = hora
        self.minutos = minuto

    def alterar_hora(self):
        nova_hora = int(input('Digite o novo horário (no formato 00): '))
        if 0 <= nova_hora <= 24:
            self.horas = nova_hora
        else: 
            print('Horário inválido. Tente novamente.')
            return self.alterar_hora()

    def alterar_minuto(self):
        novo_minuto = int(input('Digite os novos minutos: '))
        if 0 <= novo_minuto <= 60:
            self.minutos = novo_minuto
        else:
            print('Horário inválido. Tente novamente.')
            return self.alterar_minuto()

def main():
    hora = int(input('Digite as horas (no formato 00): '))
    minuto = int(input('Digite os minutos (no formato 00): '))
    if 0<= hora <= 24 and 0<= minuto <= 60:
        meu_relogio = Relógio_Digital_Simples(hora, minuto)
        print(f'Seu relógio: {meu_relogio.horas}:{meu_relogio.minutos}')
    else:
        print('Número inválido. Tente novamente!!')
        return main()
    while True:
        print('\n')
        opcao = int(input(''' Escolha uma das opções:
[ 1 ] mudar hora
[ 2 ] alterar minutos
[ 3 ] encerrar                                                  
'''))
        if opcao == 1:
            meu_relogio.alterar_hora()
        elif opcao == 2:
            meu_relogio.alterar_minuto()
        elif opcao == 3:
            print('Terminando...')
            break
        print(f'SEU RELÓGIO: {meu_relogio.horas}:{meu_relogio.minutos}')
            
if __name__=='__main__':
    main()
