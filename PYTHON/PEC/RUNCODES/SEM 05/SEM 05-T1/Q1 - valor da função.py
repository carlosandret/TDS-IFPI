def calcular(a, b, c):
    return 2 * a + 5 * b - c

def main():
    
    #entrada
    a = int(input('Digite o primeiro número: ').strip())
    b = int(input('Digite o segundo número: ').strip())
    c = int(input('Digite o terceiro número: ').strip())
    
    #processamento
    resultado = calcular(a, b, c)
    
    #saida
    print(f'O resultado é {resultado}')
    
if __name__ == '__main__':
    main()
