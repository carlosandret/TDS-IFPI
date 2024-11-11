# 2. Escreva um programa que leia uma lista com 100 números. Ao término da leitura o programa deve fazer a
# ordenação dos números lidos. Após a ordenação, crie uma lista onde os elementos de índice par são
# multiplicados por 3 e os elementos de índice ímpar são multiplicados com 5.
# DICA: Use a função a sorted() ou o método sort() para realizar a ordenação dos valores.

def eh_par(valor):
    return valor % 2 == 0

def main():
    lista_numeros = []
    print("Digite uma lista de 10 números inteiros:")
    for i in range(100):
        num = int(input(""))
        lista_numeros.append(num)
        
    lista_ordenada = sorted(lista_numeros)
    
    lista_final = []
    for i in range(0, len(lista_ordenada)):
        if eh_par(i):
            x = lista_ordenada[i] * 3
        else:
            x = lista_ordenada[i] * 5
        lista_final.append(x)

    print(f"lista ordenada e com índices pares multiplicados por 3 e impares por 5: {lista_final}")

if __name__=="__main__":
    main()