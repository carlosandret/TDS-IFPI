# Leia uma lista de 10 (dez) números inteiros, mostre os números, sua soma e a multiplicação.

def main():
    soma = 0
    multiplicacao = 1
    lista = []
    print("Digite uma lista de números inteiros:")
    for c in range(10):
        numero = int(input(""))
        soma += numero
        multiplicacao *= numero
        lista.append(numero)
    
    print(f"Esses são os números digitados {lista}")
    print(f"A SOMA dos números é {soma}")
    print(f"A MULTIPLICAÇÃO dos números é {multiplicacao}")
    
if __name__=="__main__":
    main()