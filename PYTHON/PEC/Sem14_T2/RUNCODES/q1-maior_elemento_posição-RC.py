# 1. Escreva um programa que leia 10 números inteiros e os armazene em uma lista. Imprima a lista, o maior
# elemento e a posição que ele se encontra.

def recebe_lista(qtd):
    lista = []
    for c in range(qtd):
        item = int(input(""))
        lista.append(item)
    return lista

def main():
    lista_numeros = recebe_lista(10)
    
    print(f"{lista_numeros}")
    
    maior_elemento = max(lista_numeros) 
    print(f"{maior_elemento}")
    print(f"{lista_numeros.index(maior_elemento)}")
    
if __name__=="__main__":
    main()