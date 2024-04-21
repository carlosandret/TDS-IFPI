def compara_valor(caracteres):
    a = 'A' <= caracteres.upper() <= 'Z'
    c = caracteres in '0123456789'
    return not (a or c)
 
def main():
    caractere = input('Digite um caractere: ').strip()
    print("Se o caractere for um símbolo, o valor é verdadeiro.")
    print('Caso contrário, o valor é falso:')
    print(compara_valor(caractere))

if __name__ == '__main__':
    main()
