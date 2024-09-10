# Leia 20 números inteiros e armazene-os numa lista. Separe os números pares na lista PAR e os números
# ímpares na lista IMPAR. Imprima as três listas.

def eh_par(num):
    return num % 2 == 0

def main():
    numeros = []
    lista_par = []
    lista_impar = []
    for c in range(20):
        num = int(input(""))
        numeros.append(num)
        if eh_par(num):
            lista_par.append(num)
        else:
            lista_impar.append(num)
            
    print(f"{numeros}")
    print(f"{lista_par}")
    print(f"{lista_impar}")
if __name__ == "__main__":
    main()