def ordenador(n1, n2, n3):
   terceiro = max(n1, n2, n3) 
   primeiro = min(n1, n2, n3)
   soma = n1 + n2 + n3
   soma_2 = terceiro + primeiro
   segundo = soma - soma_2
   return (f'{primeiro}\n{segundo}\n{terceiro}')
   
def main():
    numero1 = int(input('Digite o primeiro número: ').strip())
    numero2 = int(input('Digite o segundo número: ').strip())
    numero3 = int(input('Digite o terceiro número: ').strip())
    print('Esses são os números em ordem crescente:')
    print(ordenador(numero1, numero2, numero3))
if __name__ == '__main__':
    main()
