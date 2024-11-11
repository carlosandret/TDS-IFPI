def info_numero(code):
    return ord(code)

def main():
    caractere = input('Digite um caractere: ')
    codigo = info_numero(caractere)
    print(f'O codigo correspondente do caractere {caractere} é {codigo}')
if __name__ == '__main__':
    main()