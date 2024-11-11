def soma_digito(numero):
    u = numero % 10
    numero = numero // 10
    d = numero % 10
    numero = numero // 10
    c = numero % 10
    numero = numero // 10
    um = numero % 10
    numero = numero // 10
    dm = numero % 10
    numero = numero // 10
    cm = numero % 10
    soma = u + d + c + um + dm + cm 
    return soma

def main():
    numero = int(input(' Digite um número inteiro: '))
    if 0 < numero < 100000:
        print(f'A soma dos dígitos é {soma_digito(numero)}.') 
    else:
        print('A soma dos dígitos é -1.') 
   
if __name__ == '__main__':
    main()