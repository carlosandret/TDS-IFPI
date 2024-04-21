def area_quadrado(valor):
    a = valor**2
    return a

def Perimetro(valor):
    p = 4 * valor
    return p

def main():
    #entrada
    lado = float(input('Digite o lado do quadrado: ').strip())

    #processamento
    area = area_quadrado(lado)
    perimetro = Perimetro(lado)

    #saída
    print(f'O resultado da área é {area:10.4f}')
    print(f'O resultado do perímetro é {perimetro: 10.4f}')

if __name__ == '__main__':
    main()

    
