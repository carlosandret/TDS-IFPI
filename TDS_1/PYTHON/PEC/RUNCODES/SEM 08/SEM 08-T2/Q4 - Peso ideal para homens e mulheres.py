def peso_ideal_homens(altura):
    return (72.7 * altura) - 58

def peso_ideal_mulher(altura):
    return (62.1 * altura) - 44.7

def main():
    altura = float(input(' Digite a sua altura: '))
    sexo = input(' Digite o seu sexo, (1 - masculino ou 2 - feminino): ')
    print('O seu peso ideal é:')
    if sexo == '1':
        print(f'{peso_ideal_homens(altura):.2f}')
    else:
        print(f'{peso_ideal_mulher(altura):.2f}')
if __name__ == '__main__':
    main()