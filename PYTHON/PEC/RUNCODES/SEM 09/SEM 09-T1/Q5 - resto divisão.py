def verifica_impar_par(num):
    return 'par' if num % 2 == 0 else 'ímpar'

def main():
    numero = int(input(' Digite um número inteiro: '))
    resto = numero % 5
    if resto == 0:
        resultado = (9 * numero) + 7
    elif resto == 1:
        resultado = verifica_impar_par(numero)
    elif resto == 2:
        resultado = (5 * numero ** 2) - (3 * numero) + 42
    elif resto == 3:
        resultado = numero // 10
    else:
        resultado = numero ** 2
    print(f'O resultado é {resultado}.')
if __name__ == "__main__":
    main()