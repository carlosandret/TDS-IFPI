def eh_impar(valor):
    return valor % 2 == 1

def main():
    numero = int(input('Digite um número: ').strip())
    resultado = eh_impar(numero)
    print('Se der True é impar, caso contrário será par:')
    print(f'{resultado}')
if __name__ == '__main__':
    main()