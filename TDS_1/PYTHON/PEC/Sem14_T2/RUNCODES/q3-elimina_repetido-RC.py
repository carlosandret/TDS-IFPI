# 3. Escreva um programa que leia uma lista com 20 números inteiros. Escreva os elementos da lista eliminando
# elementos repetidos.

def recebe_lista(qtd):
    lista = []
    for c in range(qtd):
        item = int(input(""))
        lista.append(item)
    return lista


def main():
    lista_numeros = recebe_lista(3)

    for c in range(0, len(lista_numeros)):
        if lista_numeros[c] in lista_numeros[: c]:
            lista_numeros.remove(lista_numeros[c])
            
    print(lista_numeros)
if __name__=="__main__":
    main()