def contador_caracteres(caracter):
    caracter = caracter.strip()
    return len(caracter)

def main():
    frase = input('Digite uma frase: ').strip()
    resultado = contador_caracteres(frase)
    print(f'O número de caracteres nessa frase é {resultado}.')
if __name__ == '__main__':
    main()