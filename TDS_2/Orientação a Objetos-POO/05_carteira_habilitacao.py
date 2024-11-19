# Utilizando o processo de abstração, implemente uma classe em python que represente uma
# carteira de habilitação. Identifique atributos mutáveis e imutáveis, implemente um construtor
# da classe e métodos para manipulação dos atributos mutáveis. Faça todas as validações
# possíveis. Crie objetos para testar os métodos implementados.

# Carlos
class CNH:
    def __init__(self ,nome , validade, categoria, cpf, observacoes = 'Sem observações'):
        self.nome = nome
        self.validade = validade
        self.validar_categoria(categoria)
        self.cpf = cpf
        if observacoes != None:
            self.observacoes = observacoes
        else: self.observacoes = self.observacoes
        
    def mudar_nome(self, nome):
        self.nome = nome
        
    def mudar_categoria(self, categoria):
        self.categoria = self.validar_categoria(categoria)
        
    def mudar_observacoes(self, obs):
        self.observacoes = obs
    
    def validar_categoria(self, tipo):
        if tipo.upper() in 'ABACADAE':
            self.categoria = tipo.upper()
        else: raise ValueError('Digite uma categoria existente!')

    def __str__(self):
        s1 = f'"======== CARTEIRA DE HABILITAÇÃO ========"\n\nNome: {self.nome}\nValidade: {self.validade}\n'
        s2 = f'Categoria: {self.categoria}\nCpf: {self.cpf}\nObservações: {self.observacoes}'
        return s1+s2
        
def main():
    minha_cnh = CNH('Carlos André', '06/10/2034', 'c', '000.888.999-33')
    print(minha_cnh)
    while True:
        opcao = int(input('''\nEscolha uma opção:
    [ 1 ] Alterar nome
    [ 2 ] Mudar categoria
    [ 3 ] Acrescentar observações
    [ 4 ] Terminar
    --> '''))
    
        if opcao == 1:
            minha_cnh.nome = input('\nDigite o nome: ')
        elif opcao == 2:
            tipo = input('\nDigite a nova categoria: ')
            minha_cnh.validar_categoria(tipo)
        elif opcao == 3:
            minha_cnh.observacoes = input('\nDigite as observações: ')
        elif opcao == 4: break
        print(minha_cnh)    
        
    
if __name__=='__main__':
    main()
