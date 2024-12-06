estacoes = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}


class RadioFM:
    def __init__(self, vol_max, estacoes):
        self.__volume_min = 0
        self.__volume_max = vol_max
        self.__freq_min = 88
        self.__freq_max = 108
        self.__estacoes = list(estacoes.items())
        self.volume = None
        self.ligado = False
        self.estacao_atual = None
        self.frequencia_atual = None
        self.antena_habilitada = False

    @property
    def volume_min(self):
        return self.__volume_min

    @property
    def volume_max(self):
        return self.__volume_max

    @property
    def freq_min(self):
        return self.__freq_min

    @property
    def freq_max(self):
        return self.__freq_max

    @property
    def estacoes(self):
        return self.__estacoes

    def ligar(self):
        self.ligado = True

        if self.antena_habilitada == True:
            self.__volume_min = 1

        # Inicializa a primeira estação do dicionário
        self.frequencia_atual = self.__estacoes[0][0]
        self.estacao_atual = self.__estacoes[0][1]

    def desligar(self):
        self.ligado = False
        self.volume = None
        self.frequencia_atual = None
        self.estacao_atual = None

    def aumentar_volume(self, valor = 1):
        # 
        if valor != 1 and valor not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if self.__volume_min <= valor <= self.__volume_max:
                self.volume = valor
            else:
                print('Esse valor está fora do limite de volume!!')
        
        elif valor == 1:
            novo_volume = self.volume + valor
            if self.__volume_min <= novo_volume <= self.__volume_max:
                self.volume = valor
            else: 
                print('O valor de volume ultrapassou o limite!!')

    def diminuir_volume(self):
        pass

    def mudar_frequencia(self):
        pass


def main():
    meu_radio = RadioFM(100, estacoes)
    meu_radio.ligar()

    print(meu_radio.frequencia_atual)
    print(meu_radio.estacao_atual)


if __name__ == '__main__':
    main()
