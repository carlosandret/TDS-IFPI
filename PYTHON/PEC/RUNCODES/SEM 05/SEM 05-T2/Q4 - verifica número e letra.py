def compara_valor(caracteres):
    return 'A' <= caracteres.upper() <= 'Z' or caracteres in '0123456789'
 
def main():
    caractere = input('Digite um caractere: ').strip()
    print("Se o caractere for uma letra ou um número, o valor é verdadeiro.")
    print('Caso contrário, o valor é falso:')
    print(compara_valor(caractere))

if __name__ == '__main__':
    main()
