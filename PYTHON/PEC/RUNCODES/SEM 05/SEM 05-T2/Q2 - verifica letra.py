def compara_letra (caracteres):
    return 'A' <= caracteres.upper() <= 'Z'

def main():
    caractere = input('Digite um caractere: ').strip()
    print("Se o caractere for uma letra, o valor é verdadeiro.")
    print('Caso contrário, o valor é falso:')
    print(compara_letra(caractere))
    
if __name__ == '__main__':
    main()
