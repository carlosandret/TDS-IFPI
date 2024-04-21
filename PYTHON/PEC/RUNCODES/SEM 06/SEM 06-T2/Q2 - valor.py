def arredonda_valor(vl):
    n1 = round(vl)
    return n1

def main():
    valor = float(input('Digite uma quantidade de dinheiro: ').strip())
    resultado = arredonda_valor(valor)
    print(f'Esse valor arredondado é {resultado}.')
if __name__ == '__main__':
    main()