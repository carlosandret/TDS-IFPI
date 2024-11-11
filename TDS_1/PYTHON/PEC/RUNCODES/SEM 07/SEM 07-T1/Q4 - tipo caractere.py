def leitor(str):
    if str.upper() in 'AEIOU':
        return 'vogal'
    elif str.upper() in 'BCDFGHJKLMNPQRSTVWXYZ':
        return 'consoante'
    elif str in '0123456789':
        return 'número'
    else:
        return 'símbolo'
    
def main():
    caractere = input('Digite um caractere: ').strip()
    resultado = leitor(caractere)
    print(f'Esse caractere é do tipo {resultado}.')
if __name__ == '__main__':
    main()