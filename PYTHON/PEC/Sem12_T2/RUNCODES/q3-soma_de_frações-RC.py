# Sendo H = 1 + 1/2 + 1/3 + 1/4 + ⋯ + 1/n, escreva um programa para calcular o valor de H. O número n é lido.

def main():
    n = int(input(""))
    soma = 0
    while n != 0:
        valor = 1 / n
        soma += valor
        n = n-1
    
    print(f"{soma:.4f}")
if __name__=="__main__":
    main()