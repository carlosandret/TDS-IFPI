# 2. Implemente a classe Bicicleta, colocando limites máximos e mínimos para os estados: veloc_atual,
# altura_cela e calibragem_pneus através de seus respectivos métodos. Altere os métodos: regular_cela,
# calibrar_pneus para permitirem as mudanças caso a bicicleta esteja parada (veloc_atual=0).

class biscicleta:
    def __init__(self, veloc_atual, altura_cela, calibragem_pneus):
        self.veloc_atual  = veloc_atual
        self.altura_cela = altura_cela
        self.calibragem_pneus = calibragem_pneus
        
        if not 0 <= self.veloc_atual <= 20:
            return 'Velocidade inválida!'
        if not 0 <= self.altura_cela <= 30:
            return 'Altura da cela inválida!'
        if not 0 <= self.calibragem_pneus <= 28:
            return 'Calibragem de pneus inválida!'
        
    def regular_cela(self, medida):
        self.altura_cela += medida
        return self.altura_cela
        
    def calibrar_pneus(self, medida):
        self.calibragem_pneus += medida
        return self.calibragem_pneus

def main():
    velocidade = int(input("Velocidade da biscicleta em Km/h: "))
    altura = int(input("Altura da cela em cm: "))
    calibragem = int(input("Calibragem dos pneus em libras: "))
    minha_bicicleta = biscicleta(velocidade, altura, calibragem)
    
    
    print(f'Velocidade: {minha_bicicleta.veloc_atual}Km/h')
    print(f'Altura da cela: {minha_bicicleta.altura_cela}cm')
    print(f'Calibragem pneus: {minha_bicicleta.calibragem_pneus}lb')

    print(f'Nova altura de cela: {minha_bicicleta.regular_cela(-6)}')
    print(f'Nova calibragem: {minha_bicicleta.calibragem_pneus}')
    
if __name__=='__main__':
    main()