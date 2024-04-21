def compara_consoante(caracteres):
    return caracteres.upper() in 'BCDFGHJKLMNPQRSTVWXYZ'
 
def main():
    caractere = input('Digite um caractere: ').strip()
    print("Se o caractere for uma consoante, o valor é verdadeiro.")
    print('Caso contrário, o valor é falso:')
    print(compara_consoante(caractere))

if __name__ == '__main__':
    main()

    