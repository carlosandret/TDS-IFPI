def calcula(a, b, op):
    if op == "1":
        resultado = a + b
    elif op == "2":
        resultado = a -b
    elif op == "3":
        resultado = a * b
    else:
        resultado = a / b
    return resultado
def main():
    n1 = int(input(' Digite um número inteiro: '))
    n2 = int(input(' Digite outro número inteiro: '))
    operacao = input(' Escolha a operação (1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão): ').strip()
    print(f' O resultado é {calcula(n1, n2, operacao)}')

if __name__ == "__main__":
    main()