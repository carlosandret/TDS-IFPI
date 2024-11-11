def calcula_imc(massa, altura):
    return massa / altura**2

def main():
    m = float(input(' Digite a sua massa em kg: ')) 
    h = float(input(' Digite a sua altura em metros: '))
    imc = calcula_imc(m, h)
    print(f'O seu IMC é {imc:.2f}.')
    if imc < 18.5:
        print('Abaixo do peso')
    if 18.5 < imc < 25:
        print('Peso normal')
    if 25 < imc < 30:
        print('Sobrepeso')
    if 30 < imc < 35:
        print('Obeso leve')
    if 35 < imc < 40:
        print('Obeso moderado')
    if imc >= 40:
        print('Obeso mórbido')

if __name__ == '__main__':
    main()