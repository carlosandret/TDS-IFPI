# Avaliação POO
# Dupla: 
# - Carlos André Teixeira de Moura
# - Luis Henrique Nunes Araújo 

tipos_cafe = ['expresso', 'cappuccino',
'latte']

class MáquinaDeCafé:
    def __init__(self, capacidade_reservatorio, temperatura_max, ordem = 0):
        self.nivel_agua = 0
        self.__capacidade_reservatorio = capacidade_reservatorio
        self.__tipo_cafe = None
        self.__temperatura = 0
        self.ligado = False
        self.__temperatura_min = 70
        self.__temperatura_max = temperatura_max
        self.nivel_min_cafe = 50
        self.ordem = ordem
        
    @property
    def capacidade_reservatorio(self):
        return self.__capacidade_reservatorio
    @property
    def tipo_cafe(self):
        return self.__tipo_cafe
    @property
    def temperatura(self):
        return self.__temperatura
    @property
    def temperatura_min(self):
        return self.__temperatura_min
    @property
    def temperatura_max(self):
        return self.__temperatura_max
        
    def compara_valor(self, valor, min, max):
        return min <= valor <= max
    
    def ligar(self):
        if not self.ligado:
            self.ligado = True
        else:
            print('## A cafeteira já está ligada!')

    def desligar(self):
        if self.ligado:
            self.ligado = False
        else:
            print('## A cafeteira já está desligada!')

    def adicionar_agua(self, quantidade):
        capacidade = quantidade + self.nivel_agua
        if capacidade <= self.__capacidade_reservatorio:
            self.nivel_agua += quantidade
    
    def aquecer_agua(self, temperatura):
        nova_temp = self.__temperatura + temperatura
        if self.__temperatura_min <= nova_temp <= self.__temperatura_max:
            self.__temperatura = nova_temp

    def selecionar_tipo(self, tipo):
        if tipo in tipos_cafe:
            self.__tipo_cafe = tipo
        else:
            print('## Tipo indiponível!!')

    def preparar_cafe(self, quantidade = 0):
        if self.ligado:
            if self.compara_valor(self.temperatura, self.__temperatura_min, self.__temperatura_max):
                if self.__tipo_cafe != None:
                    if quantidade == 0:
                        if self.nivel_agua >= self.nivel_min_cafe:
                            print(f'Café de {self.nivel_min_cafe} ml pronto!!')
                            self.nivel_agua -= self.nivel_min_cafe
                        else: print('## Nível insuficiente de água!')
                    else:
                        if self.nivel_agua >= quantidade:
                            print(f'Um café de {quantidade} ml pronto!!')
                            self.nivel_agua -= quantidade
                        else: print('## Nível insuficiente de água! ):')
                else: print('## Tipo de café não selecionado!!')
            else: print('## A temperatura não está correta para fazer o café')
        else: print('## A máquina está desligada!')

    def __str__(self):
        a = f'\n## Cafeteira {self.ordem}\nEstado da máquina: {self.ligado}\nNível de água: {self.nivel_agua} ml\n'
        b = f'Temperatura: {self.temperatura} graus\nTipo de café: {self.tipo_cafe}\n'
        return a+b

def main():
    maquina_1 = MáquinaDeCafé(1000, 100, 1)
    maquina_2 = MáquinaDeCafé(1500, 100, 2)
    maquina_3 = MáquinaDeCafé(2000, 110, 3)

    print(maquina_1)
    maquina_1.ligar()
    print(maquina_1)
    maquina_1.selecionar_tipo('expresso')
    print(maquina_1)
    maquina_1.adicionar_agua(500)
    print(maquina_1)
    maquina_1.aquecer_agua(80)
    print(maquina_1)
    maquina_1.preparar_cafe()
    print(maquina_1)
    maquina_1.desligar()
    print(maquina_1)
    maquina_1.preparar_cafe()
    print(maquina_1)

    print(maquina_2)
    maquina_2.ligar()
    print(maquina_2)
    maquina_2.selecionar_tipo('cappuccino')
    print(maquina_2)
    maquina_2.adicionar_agua(600)
    print(maquina_2)
    maquina_2.aquecer_agua(80)
    print(maquina_2)
    maquina_2.preparar_cafe()
    print(maquina_2)
    maquina_2.desligar()
    print(maquina_2)
    maquina_2.preparar_cafe()
    print(maquina_2)

    print(maquina_3)
    maquina_3.ligar()
    print(maquina_3)
    maquina_3.selecionar_tipo('latte')
    print(maquina_3)
    maquina_3.adicionar_agua(250)
    print(maquina_3)
    maquina_3.aquecer_agua(40)
    print(maquina_3)
    maquina_3.preparar_cafe()
    print(maquina_3)
    maquina_3.desligar()
    print(maquina_3)
    maquina_3.preparar_cafe()
    print(maquina_3)
if __name__=='__main__':
    main()
