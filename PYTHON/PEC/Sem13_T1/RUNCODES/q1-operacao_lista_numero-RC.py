# Leia uma lista de 10 (dez) números inteiros, mostre os números, sua soma e a multiplicação.

def main():
    soma = 0
    multiplicacao = 1
    lista = []
    
    for c in range(10):
        numero = int(input(""))
        soma += numero
        multiplicacao *= numero
        lista.append(numero)
    
    print(f"{lista}")
    print(f"{soma}")
    print(f"{multiplicacao}")
    
if __name__=="__main__":
    main()