def sep_numero(numero):
    if 0 < numero < 1000:
        u = numero % 10
        numero //= 10
        d = numero % 10
        numero //= 10
        c = numero % 10
    return c, d, u

def centenas(c):
    if c == 1:
        r = 'uma centena'
    elif c == 2:
        r = 'duas centenas'
    elif c == 3:
        r = 'três centenas'
    elif c == 4:
        r = 'quatro centenas'
    elif c == 5:
        r = 'cinco centenas'
    elif c == 6:
        r = 'seis centenas'
    elif c == 7:
        r = 'sete centenas'
    elif c == 8:
        r = 'oito centenas'
    else:
        r = 'nove centenas'
    return r

def dezenas(d):
    if d == 1:
        r = 'uma dezena'
    elif d == 2:
        r = 'duas dezenas'
    elif d == 3:
        r = 'três dezenas'
    elif d == 4:
        r = 'quatro dezenas'
    elif d == 5:
        r = 'cinco dezenas'
    elif d == 6:
        r = 'seis dezenas'
    elif d == 7:
        r = 'sete dezenas'
    elif d == 8:
        r = 'oito dezenas'
    else:
        r = 'nove dezenas'
    return r

def unidades(u):
    if u == 1:
        r = 'uma unidade'
    elif u == 2:
        r = 'duas unidades'
    elif u == 3:
        r = 'três unidades'
    elif u == 4:
        r = 'quatro unidades'
    elif u == 5:
        r = 'cinco unidades'
    elif u == 6:
        r = 'seis unidades'
    elif u == 7:
        r = 'sete unidades'
    elif u == 8:
        r = 'oito unidades'
    else:
        r = 'nove unidades'
    return r
    
def main():
    numero = int(input(' Digite um número inteiro menor que 1000: '))
    cen, dez, un = sep_numero(numero)
    centena = centenas(cen)
    dezena = dezenas(dez)
    unidade = unidades(un)
    print('O número possui:')
    # tem todas as unidades
    if cen > 0 and dez > 0 and un > 0:
        print(f'{centena}, {dezena} e {unidade}.')
    # somente unidade
    elif cen == 0 and dez == 0 and un > 0:
        print(f'{unidade}.')
    # somente dezena
    elif cen == 0 and dez > 0 and un == 0:
        print(f'{dezena}.')
    # somente centena
    elif cen > 0 and dez == 0 and un == 0:
        print(f'{centena}.')
    # tem dezena e unidade
    elif cen == 0 and dez > 0 and un > 0:
        print(f'{dezena} e {unidade}.')
    # tem centena e dezena
    elif cen > 0 and dez > 0 and un == 0:
        print(f'{centena} e {dezena}.')
    # tem centena e unidade
    elif cen > 0 and dez == 0 and un > 0:
        print(f'{centena} e {unidade}.')

if __name__ == "__main__":
    main()