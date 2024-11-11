def preco_avista(var):
    return var - (var * 9/100)

def prestacao(var):
    return var / 5
    
def prestacao_10(var):
    v = (var + (var*17/100))/10
    return v

def main():
    valor = float(input('Digite o valor da compra: ').strip())
    p_avista = preco_avista(valor)
    prestacao_5 = prestacao(valor)
    prestacao_juros = prestacao_10(valor)
    print(f'O valor do pagamento a vista é {p_avista:.2f}.')
    print(f'O valor à prestação de 5 vezes é {prestacao_5:.2f}.')
    print(f'O valor à prestação de 10 vezes é {prestacao_juros:.2f}.')
if __name__ == '__main__':
    main()