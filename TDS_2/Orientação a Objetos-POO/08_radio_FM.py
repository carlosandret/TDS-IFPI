estacoes = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}
frequencias = [89.5, 91.5, 94.1, 99.1]

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
    
    def verifica_limite_volume(self, valor):
        return self.__volume_min <= valor <= self.__volume_max
    
    def habilita_antena(self):
        self.antena_habilitada = True
    
    def confere_nao_e_letra(self, texto):
        return not texto.isalpha()

    def ligar(self):
        self.ligado = True
        # Verifica se a antena esta conectada
        if self.antena_habilitada == True:
            self.volume = self.__volume_min
            # Inicializa a primeira estação do dicionário
            self.frequencia_atual = self.__estacoes[0][0]
            self.estacao_atual = self.__estacoes[0][1]

    def desligar(self):
        if self.ligado == True:
            # Desliga o radio e reseta os atributos
            self.ligado = False
            self.volume = self.volume_min
            self.frequencia_atual = None
            self.estacao_atual = None
            
        else: print('O rádio já está desligado!!')    

    def aumentar_volume(self, valor = 1):
        if self.ligado == True:
            # Caso o valor seja diferente de 1
            if valor != 1 and self.confere_nao_e_letra(str(valor)):
                novo_volume = self.volume + valor
                # Verifica se o valor está entre o limite
                if self.verifica_limite_volume(novo_volume):
                    self.volume = novo_volume
                else:
                    print('Esse valor está fora do limite de volume!!')                                  
            # Caso o valor seja igual a 1
            elif valor == 1:
                novo_volume = self.volume + valor
                if self.verifica_limite_volume(novo_volume):
                    self.volume = novo_volume
                else: 
                    print('O valor de volume ultrapassou o limite!!')                    
            # Caso seja digitado algo diferente de número
            else:
                print('Digite um valor válido!!')
        else: print('Não pode alterar o volume de o rádio estiver desligado!!')

    def diminuir_volume(self, valor = 1):
        if self.ligado == True:
            # Caso o valor seja diferente de 1
            if valor != 1 and self.confere_nao_e_letra(str(valor)):
                novo_volume = self.volume - valor
                # Verifica se o valor está entre o limite
                if self.verifica_limite_volume(novo_volume):
                    self.volume = novo_volume
                else: print('Esse valor está fora do limite de volume!!')                                    
            # Caso o valor seja igual a 1
            elif valor == 1:
                novo_volume = self.volume - valor
                if self.verifica_limite_volume(novo_volume):
                    self.volume = novo_volume
                else: 
                    print('O valor de volume ultrapassou o limite!!')                    
            # Caso seja digitado algo diferente de número
            else:
                print('Digite um valor válido!!')    
        else: print('Não pode alterar o volume de o rádio estiver desligado!!')
        
        
        
    def mudar_frequencia(self, frequencia = 0):
        if self.ligado == True:
            # Confere se o parâmetro é diferente de zero e se é um número
            if frequencia != 0 and self.confere_nao_e_letra(str(frequencia)):
                self.frequencia_atual = frequencia
                if frequencia in estacoes:
                    self.estacao_atual = estacoes[frequencia]
                else: 
                    self.estacao_atual = 'estação inexistente'
            # Caso não seja colocado parâmetro   
            else:
                prox_indice = 1
                # Faz a busca do indice correspondente na lista
                indice_atual = frequencias.index(self.frequencia_atual)
                # Se o indice for maior que o da última frequência ele retorna para o da primeira frequência
                if indice_atual >= len(frequencias)-1:
                    prox_indice = 0
                    self.frequencia_atual = frequencias[prox_indice]
                    self.estacao_atual = estacoes[self.frequencia_atual]
                else:
                    # Se o indice for menor do que o da última frequência ele passa para a próxima
                    prox_indice += indice_atual
                    self.frequencia_atual = frequencias[prox_indice]
                    self.estacao_atual = estacoes[self.frequencia_atual]
                    
        else: print('O radio deve star ligado para mudar a frequência!!')
    
    def __str__(self):
        a = f'\nRadio FM \n{'-'*30}\nStatus do radio: {self.ligado}\nVolume: {self.volume}'
        b = f'\nFrequênia atual: {self.frequencia_atual}\nEstação atual: {self.estacao_atual}'
        c = f'\nAntena habilitada: {self.antena_habilitada}\n'
        return a+b+c


def main():
    meu_radio = RadioFM(100, estacoes)
    meu_radio.habilita_antena()
    meu_radio.ligar()
    print(meu_radio)
    meu_radio.aumentar_volume(60)
    print(meu_radio)
    meu_radio.diminuir_volume(20)
    print(meu_radio)
    meu_radio.aumentar_volume()
    print(meu_radio)
    meu_radio.mudar_frequencia()
    print(meu_radio)
    meu_radio.mudar_frequencia()
    print(meu_radio)
    meu_radio.mudar_frequencia(89.5)
    print(meu_radio)
    meu_radio.desligar()
    print(meu_radio)
    meu_radio.diminuir_volume()
    print(meu_radio)
if __name__ == '__main__':
    main()
