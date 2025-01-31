class ContaCorrente:
    def __init__(self, numero, saldo = 0):
        self.numero = numero
        self.__saldo = saldo
                
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    def confere_se_numero(self, valor):
        return type(valor) != str
    
    def creditar(self, valor):
        try:
            self.confere_se_numero(valor)
            self.__saldo += valor 
        except: 
            print('\nErro: O valor deve ser numérico!')
        
    def debitar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else: print('Erro: __Saldo insuficiente!!')
    
    def transferir(self, valor, conta_destino):
        if self.__saldo >= valor:
            if type(conta_destino) == ContaCorrente:
                conta_destino.__saldo += valor
            else: print('Erro: Digite uma conta válida!!')      
        else: print('Erro: Não foi possível tranferir, Saldo insuficiente!!')
    
    def __str__(self):
        return f'\nNúmero da conta: {self.numero}\nSaldo: R$ {self.__saldo}'
        

class ContaPoupança(ContaCorrente):
    def __init__(self, numero, saldo, taxa_juros):
        super().__init__(numero, saldo)
        self.__taxa_juros = taxa_juros

    @property
    def taxa_juros(self):
        return self.__taxa_juros
    
    def render_juros(self):
        juros = (self.__taxa_juros/100) * self.saldo
        self.saldo += juros
    
    def __str__(self):
        return f'{super().__str__()}\nTaxa de juros: {self.__taxa_juros}%'

def main():
    conta1 = ContaCorrente(1234)
    conta2 = ContaPoupança(2222, 100, 10)

    print(conta2)
    conta2.render_juros()
    print(conta2)
main()