def inverso (numero):
    unidade = numero % 10
    numero =  numero // 10
    dezena = numero % 10
    numero = numero // 10
    centena = numero % 10
    numero = numero // 10
    milhar = numero % 10 
    return (unidade * 1000) + (dezena * 100) + (centena * 10) + milhar

def main():
    num = int(input('Digite um número entre 1000 e 9999: ').strip())
    numero_invertido = inverso (num)
    print(f'Este número na ordem inversa é {numero_invertido}')

if __name__ == '__main__':
    main()
