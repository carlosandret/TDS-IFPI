def leitor_numero(valor):
    n = 0
    if (valor % 10) % 2 == 0:
        n = 1
    valor = valor // 10
    if (valor % 10) % 2 == 0:
        n = n + 1
    valor = valor // 10
    if valor > 0:
        if valor % 2 == 0:
         n = n + 1
    return n

def main():
    numero = int(input('Digite um número inteiro entre 100 e 999: ').strip())
    print(f'A quantidade de números pares é {leitor_numero(numero)}.')
if __name__ == '__main__':
    main()