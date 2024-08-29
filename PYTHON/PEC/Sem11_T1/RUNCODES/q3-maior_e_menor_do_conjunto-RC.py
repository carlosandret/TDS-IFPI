# Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo número 0 (zero). 
# Ao final, o programa deve mostrar o maior e o menor de todos os números lidos (excluindo o zero).


def main():
    numeros = []
    while True:
        num = int(input(""))
        numeros.append(num)
        if num == 0: break
    numeros.remove(0)
    print(f"{max(numeros)}")
    print(f"{min(numeros)}")


if __name__=="__main__":
    main()