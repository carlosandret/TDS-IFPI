def main():
    numero = int(input('Digite um número correspondente (1-domingo, 2-segunda-feira, 3-terça-feira, 4 quarta-feira etc.) '))
    if numero == 1:
        resultado = 'domingo'
    elif numero == 2:
        resultado = 'segunda-feira'
    elif numero == 3:
        resultado = 'terça-feira'
    elif numero == 4:
        resultado = 'quarta-feira'
    elif numero == 5:
        resultado = 'quinta-feira'
    elif numero == 6:
        resultado = 'sexta-feira'
    elif numero == 7:
        resultado = 'sábado'
    else:
        resultado = 'valor inválido'
    print(resultado)
if __name__ == "__main__":
    main()