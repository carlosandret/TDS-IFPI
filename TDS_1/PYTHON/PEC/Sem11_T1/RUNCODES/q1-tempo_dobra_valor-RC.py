# Escreva um programa que pergunte o depósito inicial e a taxa de juros ao ano de uma poupança. Mostre
# em quantos anos o valor acumulado será o dobro do valor inicial.

def main():
    deposito = float(input("").strip())
    taxa_ano = float(input("").strip())
    x = 2 * deposito
    
    anos = 0
    while deposito <= x:
        taxa = taxa_ano / 100 * deposito
        deposito += taxa
        anos += 1
    print(f"{anos}")
    


if __name__ == '__main__':
    main()