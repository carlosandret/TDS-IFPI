
def calcula_acrescimo (valor, porcentagem):
    return valor + (valor * (porcentagem/100))

def calcula_desconto (valor, porcentagem):
    return valor - (valor * (porcentagem/100))

def main():
    #Entrada
    preço = float(input('Digite o valor: ').strip())
    Porcent = float(input('Digite o valor perventual %: ').strip())

    #Processamento
    Acrescimo = calcula_acrescimo (preço, Porcent)
    Desconto = calcula_desconto (preço, Porcent)

    #Saída
    print(f'O preço acrescido do percentual é {Acrescimo:.2f}')
    print(f'O preço com o desconto percentual é {Desconto:.2f}')

if __name__ == '__main__':
    main()

