# Definir um código principal com a criação de pelo menos 3 objetos (Pessoas). Fazer a adoção de pets "de rua" e de pets "de abrigos". Simular a perda de um deles e a consequente atualização (remoção) da lista de pets


class Pet:
  def __init__(self,tipo,nome,idade,peso,raca,cor,castrado=False):
    self.__tipo = tipo
    self.__nome = nome
    self.__idade = idade
    self.__peso = peso
    self.__raca = raca
    self.__cor = cor
    self.__castrado = castrado
    

class Pessoa:
  def __init__(self,cpf,nome,endereço):
    self.__cpf = cpf
    self.__nome = nome
    self.__endereço = endereço
    self.__meus_pets = []
    
  @property
  def cpf(self):
    return self.__cpf
  @property
  def nome(self):
    return self.__nome
  @property
  def endereço(self):
    return self.__endereço
  @property
  def meus_pets(self):
    return self.__meus_pets
  

  def cadastrar_pet(self,pet):
   pass

  def excluir_pet(self,nome):
    pass

  def mostrar_meus_pets(self):
    pass


def main():
    pass
    
if __name__=='__main__':
    main()