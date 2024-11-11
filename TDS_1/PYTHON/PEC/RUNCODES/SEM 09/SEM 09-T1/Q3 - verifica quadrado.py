def main():
    base = int(input(' Digite o valor da base: '))
    altura = int(input(' Digite o valor da altura: '))
    resultado = "QUADRADO" if base == altura else (f"{2 * altura + 2 * base} - {altura *base}")
    print(f'A respota é {resultado}')
if __name__ == "__main__":
    main()