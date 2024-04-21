def calculo_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if n3 > 8:
        media += 1    
    if media > 10:
        media = 10
    return media
def main():
    nota1 = float(input('Digite a primeira nota: ').strip())
    nota2 = float(input('Digite a segunda nota: ').strip())
    nota3 = float(input('Digite a terceira nota: ').strip())
    resultado = calculo_media(nota1, nota2, nota3)
    print(f'A média é {resultado}.')
if __name__ == '__main__':
    main()