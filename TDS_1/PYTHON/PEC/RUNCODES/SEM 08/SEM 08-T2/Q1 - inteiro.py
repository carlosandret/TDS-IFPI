def main():
    numero = int(input(' Digite um número inteiro: '))
    print('Irá somar 5 caso valor lido seja par ou somar 8 caso o valor lido seja ímpar.')
    if numero % 2 == 0:
        resultado = numero + 5
    elif numero % 2 == 1:
        resultado = numero + 8
    print(f' O resultado é {resultado}.') 
if __name__ == '__main__':
    main()