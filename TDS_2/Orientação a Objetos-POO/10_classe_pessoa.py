def vermelho(texto):
    return f"\033[33;31m{texto}\033[m"
def verde(texto):
    return f"\033[33;32m{texto}\033[m"

class Pessoa:
  def __init__(self,nome,idade,peso,altura,sexo,estado="vivo",est_civil="solteiro",mãe=None):
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
    if self.__est_civil == "casado":
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
    if self.__est_civil != "casado(a)":
        self.__est_civil = "casado(a)"
        #Confere se o conjuge é uma pessoa
        if type(conjuge)==Pessoa:
            self.__conjuge = conjuge
            # Modifica os atributos do cônjuge
            self.__conjuge.__est_civil = "casado(a)"
            self.__conjuge.__conjuge = self
        print(verde(f'# {self.__nome} e {self.__conjuge.__nome} se casaram com sucesso!'))
    else: print(vermelho('# Voçê já é casado, não pode casar novamente!!'))

  def morrer(self):
    if self.__estado != 'morto(a)':
        self.__estado = 'morto(a)'
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

# 2. Crie um método: "ter_filhos". Condição para este método ser executado:
# a) Pessoa ser do sexo: "Feminino"
# b) Segunda pessoa ser do sexo: "Masculino" . Ex: maria.ter_filho(joao), nesse caso maria é um objeto do tipo "Pessoa" do sexo: "feminino" e joao é um objeto do tipo "Pessoa" do sexo: "masculino". Esse método tem que retornar um novo objeto do tipo "Pessoa" 
# c) acrescentar os atributos: Pai e Mãe (tipo: Pessoa).
# d) Inserir na lista: filhos, todos os objetos gerados.

  def ter_filhos(self,pessoa):
    if self.__estado != 'morto(a)':
        if self.__sexo == 'F' and pessoa.__sexo == 'M':
            filho = Pessoa('filho',0,4,0.40,'M')
            filho.__pai = pessoa
            filho.__mãe = self
            self.filhos.append(filho)
            print(verde(f'# {self.__nome} teve um filho com sucesso!'))
            return filho       
        else:
            print(vermelho('# Só é possível que uma Mulher tenha filho com um homem!'))
    else: print(vermelho('# Não é possivel ter filhos enquanto se está morto!'))
        
  def adotar_filhos(self,criança): #condição: criança ser órfã.
    pass

  def __str__(self):
    x = f'{'-'*10} {self.__nome} {'-'*10}' 
    a = f'\nIdade: {self.__idade} anos, Estado civil: {self.est_civil}\nPeso: {self.__peso} Kg, Altura: {self.__altura}m'
    b = f'\nSexo: {self.__sexo}, Estado: {self.__estado}\nNome da mãe: {self.__mãe}, Nome do pai: {self.__pai}'
    c = f'\nMãe adotiva: {self.__mãe_adotiva}, Pai adotivo: {self.__pai_adotivo}'
    d = f'\nNome do cônjuge: {self.__conjuge.nome if self.__conjuge else None}\n'
    return x+a+b+c+d

def main():
    maria = Pessoa("Maria",30,65,1.7,'F')
    joao = Pessoa("João",25,70,1.8,'M')
    clara = Pessoa('Clara',26,64,1.65,'F')
    criança  = Pessoa('Luis', 10,40,1.40,'M')
    
    print(maria) 
    print(joao)
    
    # Maria casa com joão
    maria.casar(joao)
    print(maria)
    print(joao)
    
    # Maria e joao se divorciam
    maria.divorciar(joao)
    print(maria)
    print(joao)
    
    # Maria tem um filho com joao
    filho_maria = maria.ter_filhos(joao)
    print(filho_maria)
    print('\n')
    print(maria.filhos)
    
    
if __name__=="__main__":
    main()

####### execução ########

# maria = Pessoa("Maria",30,65,1.7,'F', Pessoa("Francisca",65,60,1.6,'F')) # maria -> solteira
# joao = Pessoa(...) # joão -> solteiro
# maria.casar(joao) # joão e maria -> casado
# ana = Pessoa(...)
# pedro = joao.ter_filhos(ana)
# joao.casar(ana) # não é possivel pois joão já é casado com maria
# maria.morrer() # maria para para o estado de morto.
# joao.casar(ana) # joao e ana -> casado
# joao.ter_filhos(maria) # Erro! maria está morta.
# julia = ana.ter_filhos(joao)

#simular processo de adoção
