def media(a, b, c, d, e):
    return (a + b + c + d + e) / 5

def maior(a, b, c, d, e):
    return max(a, b, c, d, e)

def menor(a, b, c, d, e):
    return min(a, b, c, d, e)

def main():
    num1 = int(input('Digite o primeiro número: ').strip())
    num2 = int(input('Digite o segundo número: ').strip())
    num3 = int(input('Digite o terceiro número: ').strip())
    num4 = int(input('Digite o quarto número: ').strip())
    num5 = int(input('Digite o quinto número: ').strip())
    Maior = maior(num1, num2, num3, num4, num5)
    Menor = menor(num1, num2, num3, num4, num5)
    Media = media(num1, num2, num3, num4, num5)
    print(f'O maior dos números é {Maior}.')
    print(f'O menor dos números é {Menor}.')
    print(f'A média dos números é {Media}.')

if __name__ == '__main__':
    main()