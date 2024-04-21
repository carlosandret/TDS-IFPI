def calculo_maca(fruta):
    x = 3 * fruta
    return x
def calculo_banana(fruta):
    x = 2 * fruta
    return x

def main():
    p1 = float(input('Digite o preço de uma maçã: ').strip())
    p2 = float(input('Digite o preço de uma banana: ').strip())
    valor_m = calculo_maca(p1)
    valor_b = calculo_banana(p2)
    resultado = valor_m + valor_b
    print(f'O total da sua compra foi de {resultado:.2f}.')
if __name__ == '__main__':
    main()