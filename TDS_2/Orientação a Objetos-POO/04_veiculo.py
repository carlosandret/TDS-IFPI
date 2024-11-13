# Exercício: Classe Veiculo
# Objetivo:
# Implementar uma classe Veiculo que represente o registro de um veículo em um sistema de controle de veículos. 
# A atividade deve explorar a criação de construtores, atributos obrigatórios e opcionais, 
# e o uso de métodos para exibir e atualizar as informações do veículo.

class Veiculo:
    def __init__(self, chassi, marca, modelo, ano, placa = 'Nao especificada', cor = 'Não especificada', proprietario = 'Nao especificado', quilometragem = 0):
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo        
        self.ano = ano
        self.placa = placa
        self.cor = cor
        self.proprietario = proprietario
        self.quilometragem = quilometragem

    # Funções para alterar os parãmetros
    def mudar_cor(self, cor):
        self.cor = cor    
    def mudar_placa(self, placa):
        self.placa = placa
    def mudar_proprietario(self, proprietario):
        self.proprietario = proprietario
    def mudar_quilometragem(self, valor):
        self.quilometragem = valor
        
    def __str__(self):
        s1 = f'\nChassi: {self.chassi}\nMarca: {self.marca}\nModelo: {self.modelo}'
        s2 = f'\nAno: {self.ano}\nPlaca: {self.placa}\nCor: {self.cor}'
        s3 = f'\nProprietário: {self.proprietario}\nQuilometragem: {self.quilometragem}\n'
        return s1+s2+s3

def main():
    meu_carro = Veiculo(1234, 'sedan', 'Fiat', 2020)
    print(meu_carro) 
    while True:
        opcao = int(input('''Escolha uma opção:
    [ 1 ] Alterar cor
    [ 2 ] Alterar placa
    [ 3 ] Mudar proprierario
    [ 4 ] Mudar quilometragem 
    [ 5 ] Encerrar
    
    --> '''))
    
        if opcao == 1:
            cor = input('Digite a cor: ')
            if cor == '':
                meu_carro.cor = meu_carro.cor
            else: meu_carro.mudar_cor(cor)                
        elif opcao == 2:
            placa = input('Digite a nova placa: ')
            if placa == '':
                meu_carro.placa = meu_carro.placa
            else: meu_carro.mudar_placa()
        elif opcao == 3:
            proprietario = input('Digite o novo proprietario: ')
            if proprietario == '':
                meu_carro.proprietario = meu_carro.proprietario
            else: meu_carro.mudar_proprietario()
        elif opcao == 4:
            valor = int(input('Digite a nova quilometragem: '))
            # Limita o valor da quilometragem
            if 0 <= valor <= 300:
                meu_carro.quilometragem = valor
            else: print('Digite um valor dentro do limite!!')             
        elif opcao == 5: break
        else: print('Escolha uma opcao válida!!')
        print(meu_carro)
if __name__=='__main__':
    main()
