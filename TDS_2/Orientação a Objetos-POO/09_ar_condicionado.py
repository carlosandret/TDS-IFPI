class Ar_condicionado:
    def __init__(self, temp_max, modo = 'automático'):
        self.__temp_min = 16
        self.__temp_max = temp_max
        self.__vel_min = 1
        self.__vel_max = 10
        self.temperatura = None
        self.velocidade = None
        self.modo = modo
        self.lidado = False

    @property
    def temp_min(self):
        return self.__temp_min
    @property
    def temp_max(self):
        return self.__temp_max
    @property
    def vel_min(self):
        return self.__vel_min
    @property
    def vel_max(self):
        return self.__vel_max
        
    def ligar(self):
        self.ligado = True
        self.temperatura = self.temp_min
        self.velocidade = self.vel_min
    
    def desligar(self):
        if self.ligado:
            self.lidado = False
            self.temperatura = self.temp_min
            self.velocidade = self.vel_min
        else:
            print('O ar-condicionado já está desligado!!')
    def aumentar_temperatura(self):
        pass
    
    def aumentar_temperatura(self):
        pass
    
    def diminuir_velocide(self):
        pass
    
    def mudar_modo(modo):
        pass
    
    def __str__(self):
        pass