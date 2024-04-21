def calcula_media(n1, n2, n3, n4, n5):
    resultado = (n1 + n2 + n3 + n4 + n5) / 5
    return resultado
    
def main():
    #Entrada
    print(' Digite cinco números inteiros: ')
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())
    #Processamento
    media = calcula_media(n1, n2, n3, n4, n5)
    #Saida de dados
    print(f' A média é {media:.2f} ')
    print('Os números maiores que a média são: ')
    if n1 > media:
        print(f'{n1:.2f}') 
    if n2 > media:
        print(f'{n2:.2f}') 
    if n3 > media:
        print(f'{n3:.2f}') 
    if n4 > media:
        print(f'{n4:.2f}') 
    if n5 > media:
        print(f'{n5:.2f}') 
if __name__ == '__main__':
    main()