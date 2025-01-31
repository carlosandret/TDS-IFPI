# Classe base
from datetime import datetime
class Veiculo:
    def __init__(self, marca, modelo, ano,valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def __str__(self):
        return f"Marca:{self.marca}\nModelo: {self.modelo}\nAno:{self.ano}\nValor:{self.valor}\n"

    def ligar(self):
        return "O veículo está ligado."

    def desligar(self):
        return "O veículo está desligado."
    
    def calcula_ipva(self):
      pass
    

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, valor, portas):
        super().__init__(marca, modelo, ano, valor)
        self.portas = portas
      
    def calcula_ipva(self):
      ano_atual = datetime.now().year
      ano_fabricacao = self.ano
      idade = ano_atual - ano_fabricacao
      if idade > 10:
        return 0
      else:
        return 0.04*self.valor

    def __str__(self):
        return f"{super().__str__()}\n IPVA: {self.calcula_ipva()}\n com {self.portas} portas."


# Classe derivada: Moto
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, valor, cilindradas):
        super().__init__(marca, modelo, ano, valor)
        self.cilindradas = cilindradas
    
    def calcula_ipva(self):
      ano_atual = datetime.now().year
      ano_fabricacao = self.ano
      idade = ano_atual - ano_fabricacao
      if idade > 10:
        return 0
      else:
        return 0.02*self.valor

    def __str__(self):
        return f"{super().__str__()}\n IPVA: {self.calcula_ipva()}\n com {self.cilindradas}cc."

   
# Testando as classes
def main():
    polo = Carro("VW","Polo",2024,60000,4)
    fusca = Carro("VW","Fusca",1978,1500,2)
    moto = Moto("Honda","Pop",2015,10000,100)
    print(polo)
    print(fusca)
    print(moto)

   

if __name__ == "__main__":
    main()
