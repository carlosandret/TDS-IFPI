def leitor_numero(valor):
    n = 0
    if (valor % 10) % 2 == 1:
        n = 1
    valor = valor // 10
    if valor > 0:
        if valor % 2 == 1:
         n = n + 1
    return n

def main():
    numero = int(input('Digite um número inteiro entre 10 e 99: ').strip())
    if leitor_numero(numero) == 1:
        print('Apenas um dígito é ímpar.')
    elif leitor_numero(numero) == 2:
        print('Os dois dígitos são ímpares.') 
    else:
        print('Nenhum dígito é ímpar.')
if __name__ == '__main__':
    main()