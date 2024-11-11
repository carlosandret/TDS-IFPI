def conversor_fahren(temp):
    return (temp * (9 / 5)) + 32

def main():
    celcius = float(input('Digite a temperatura em Celsius: ').strip())
    resultado = (conversor_fahren(celcius))
    print(f"Essa temperatura em Fahrenheits é {resultado:.2f}.")
if __name__ == '__main__':
    main()