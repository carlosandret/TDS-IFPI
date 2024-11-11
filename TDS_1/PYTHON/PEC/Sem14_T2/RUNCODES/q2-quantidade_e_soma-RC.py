# 2. Escreva um programa que leia uma lista com 10 números reais, calcule e mostre a lista, a quantidade de
# números negativos e a soma dos números positivos dessa lista.

def recebe_lista(qtd):
    lista = []
    for c in range(qtd):
        item = int(input(""))
        lista.append(item)
    return lista

def main():
    lista_numeros = recebe_lista(10)
    qtd_negativo = 0
    soma_positivos = 0

    for c in lista_numeros:
        if c < 0: qtd_negativo += 1

    for c in lista_numeros:
        if c > 0: soma_positivos += c
        
    print(f"{lista_numeros}")
    print(f"{qtd_negativo}")
    print(f"{soma_positivos}")
if __name__=="__main__":
    main()