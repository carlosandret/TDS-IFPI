# Funções para alterar a cor do texto e dar destaque
def vermelho(texto):
    return f"\033[33;31m{texto}\033[m"
def verde(texto):
    return f"\033[33;32m{texto}\033[m"

class Pessoa:
  def __init__(self,nome,idade,peso,altura,sexo,estado="vivo(a)",est_civil="solteiro(a)",mãe=None):
    self.__nome = nome
    self.__idade = idade
    self.__peso = peso
    self.__altura = altura
    self.__sexo = sexo
    self.__estado = estado
    self.__est_civil = est_civil
    self.__mãe = mãe
    self.__pai = None
    self.__mãe_adotiva = None
    self.__pai_adotivo = None
    self.__conjuge = None
    self.filhos = []

  @property
  def nome(self):
    return self.__nome
  
  @property
  def conjuge(self):
    return self.__conjuge
  @property
  def est_civil(self):
    return self.__est_civil
  @nome.setter
  def nome(self,valor):
    if self.__est_civil == "casado(a)":
      nome_antigo = self.__nome.split(" ")
      nome_conjuge = self.__conjuge.nome.split(" ")
      novo_nome = valor.split(" ")
      for i in novo_nome:
        if (i not in nome_antigo) and (i not in nome_conjuge):
           print(vermelho("# Nome inválido!"))
           return
      self.__nome = valor
      print (verde("# Alteração efetuada com sucesso!"))
  
# 1. Altere o código de forma a impedir que uma pessoa "casada"  possa se casar novamente. Exceções: Quando a pessoa se tornar "viúva" ou "divorciada"
  def casar(self,conjuge):
    if type(conjuge)==Pessoa:
      if self != conjuge:
        if self.__estado != 'morto(a)' and conjuge.__estado != 'morto(a)':
          if self.__est_civil != "casado(a)" and conjuge.__est_civil != 'casado(a)':
              self.__est_civil = "casado(a)"
              #Confere se o conjuge é uma pessoa
              self.__conjuge = conjuge
              # Modifica os atributos do cônjuge
              self.__conjuge.__est_civil = "casado(a)"
              self.__conjuge.__conjuge = self
              print(verde(f'# {self.__nome} e {self.__conjuge.__nome} se casaram com sucesso!'))
          else: print(vermelho('# Voçê já é casado(a), não pode casar novamente!!'))
        else: print(vermelho('# Não é possivel se casar enquanto se está morto!'))
      else: print(vermelho('# Você não pode se casar consigo mesmo!'))

  def morrer(self):
    if self.__estado != 'morto(a)':
        self.__estado = 'morto(a)'
        self.__conjuge.__conjuge = None
        self.__conjuge.__est_civil = 'viuvo(a)'
    else:
        print(vermelho('# Você já está morto!!'))

  def divorciar(self, conjuge):
    if self.__est_civil != 'divorciado(a)':
        self.__est_civil = 'divorciado(a)'
        #Confere se o conjuge é uma pessoa
        if type(conjuge)==Pessoa:
            self.__conjuge = None
            # Modifica os atributos do cônjuge
            conjuge.__est_civil = "divorciado(a)"
            conjuge.__conjuge = None
            print(verde(f'# {self.__nome} se divorciou com sucesso!'))
        else:
          print(vermelho('# O cônjuge deve ser um objeto do tipo pessoa!'))
    else:
        print(vermelho('# Você já é divorciado(a)!'))

  def ter_filhos(self,pessoa):
    if self.__estado != 'morto(a)':
      if type(pessoa)==Pessoa:
        if self.__sexo != pessoa.__sexo:
            filho = Pessoa('filho',0,4,0.04,'M')
            filho.__pai = pessoa.__nome
            filho.__mãe = self.__nome
            self.filhos.append(filho)
            print(verde(f'# {self.__nome} teve um filho com sucesso!'))
            return filho       
        else:
            print(vermelho('# Somente pessoas de sexos diferentes podem ter filhos!'))
      else:
        print(vermelho('# O parceiro deve ser um objeto do tipo pessoa!'))
    else: 
      print(vermelho('# Não é possivel ter filhos enquanto se está morto!'))
        
  def adotar_filhos(self,criança): #condição: criança ser órfã.
    if self.__estado != 'morto(a)':
      if type(criança)==Pessoa:
        if criança.__pai == None and criança.__mãe ==None:
          if self.__sexo == 'M':
            criança.__pai_adotivo = self
            criança.__mãe_adotiva = self.__conjuge
          else:
            criança.__pai_adotivo = self.__conjuge
            criança.__mãe_adotiva = self         
        else:
          print(vermelho('# A criança já possui pais então não pode ser adotada!'))
      else:
        print(vermelho('# O parceiro deve ser um objeto do tipo pessoa!'))
    else:
      print(vermelho('# Não é possivel ter filhos enquanto se está morto!'))

  def __str__(self):
    x = f'{'-'*10} {self.__nome} {'-'*10}' 
    a = f'\nIdade: {self.__idade} anos, Estado civil: {self.est_civil}\nPeso: {self.__peso} Kg, Altura: {self.__altura}m'
    b = f'\nSexo: {self.__sexo}, Estado: {self.__estado}\nNome da mãe: {self.__mãe}, Nome do pai: {self.__pai}'
    c = f'\nMãe adotiva: {self.__mãe_adotiva.nome if self.__mãe_adotiva != None else self.__mãe_adotiva} , Pai adotivo: {self.__pai_adotivo.nome if self.__pai_adotivo != None else self.__pai_adotivo}'
    d = f'\nNome do cônjuge: {self.__conjuge.nome if self.__conjuge else None}\n'
    return x+a+b+c+d

def main():
    maria = Pessoa("Maria dos Santos",30,65,1.7,'F')
    joao = Pessoa("João mendes",25,70,1.8,'M')
    clara = Pessoa('Clara dos anjos',26,64,1.65,'F')
    criança  = Pessoa('Filho adotado', 10,40,1.40,'M')
    
    print(maria) 
    print(joao)
    
    # Maria casa com João
    maria.casar(joao)
    print(maria)
    print(joao)
    
    # João tenta se casar com Clara
    joao.casar(clara)
    print(joao)
    
    # João tem um filho com Clara
    filho_clara = clara.ter_filhos(joao)
    print(filho_clara)
    print(verde(f'Quantidade de filhos de Clara: {len(clara.filhos)}\n'))
    
    # Maria e joao se divorciam
    maria.divorciar(joao)
    print(maria)
    print(joao)
    
    # Maria tenta se divorciar novamente - ERRO!
    maria.divorciar(joao)
    
    # Maria adota um filho
    maria.adotar_filhos(criança)
    print(criança)
    print(maria)
    
    # João se casa com Clara
    joao.casar(clara)
    print(joao)
    print(clara)
    
    # Clara morre 
    clara.morrer()
    print(clara)
    print(joao)
    
    # Clara tenta se casar com joao depois de morta - ERRO!
    clara.casar(joao)
    print(clara)
    
    # João tenta ter um filho com Clara depois de morta - ERRO!
    joao.ter_filhos(clara)

    
if __name__=="__main__":
    main()
