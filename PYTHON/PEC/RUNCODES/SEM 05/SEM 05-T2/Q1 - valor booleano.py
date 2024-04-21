def compara_vogal (caracteres):
    return caracteres.upper() in 'AEIOU'
 
def main():
    caractere = input('Digite um caractere: ').strip()
    print("Se o caractere for uma vogal, o valor é verdadeiro:")
    print('Caso contrário, o valor é falso:')
    print(compara_vogal(caractere))

if __name__ == '__main__':
    main()

    