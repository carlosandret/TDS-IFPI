# 1. Exercitando o processo de abstração, modele uma classe Relógio_Digital_Simples com seus estados e
# comportamentos. Crie a respectiva classe em python e depois crie 2 objetos, imprima os valores de seus
# atributos e execute os métodos criados. Recomendação: criar estados que possam ter seus valores alterados
# por seus métodos.

class Relogio_Digital_Simples:
        def __init__(self, hora, minuto):
            self.hora = hora
            self.minuto = minuto
            
def main():
    while True:
        opcao = int(input('Escolha uma das opções: '))
    
    
    
if __name__ =="__main__":
    main()
# class Gato:
#   rg = 0
#   def __init__(self,nome,peso,idade):
#     Gato.rg += 1
#     self.rg = Gato.rg
#     self.nome = nome
#     self.peso = peso
#     self.idade = idade
    
# mimi = Gato("Mimi",0.1,0)
# print(f'Rg:{mimi.rg} Nome: {mimi.nome}')
# tom = Gato("Tom",0.5,1)
# print(f'Rg:{tom.rg} Nome: {tom.nome}')