# 4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.

from random import randint
# Função que gera uma lista aleatória com uma quantidade especificada de números, com intervalo de 1 a 50
def gera_lista(qtd_num):
    lista = []
    while len(lista) < qtd_num:
        x = randint(1, 50)
        if x not in lista:
            lista.append(x)
        continue
    return lista

# Função para encontrar o maior item de uma lista, retorna a posição e o valor do maior item
def posicao_maximo(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return lista.index(maior) + 1, maior

# Função para encontrar o menor item de uma lista, retorna a posição e o valor do menor item
def posicao_minimo(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return lista.index(menor) + 1, menor

def main():
    # ACERTOS
    assert posicao_maximo([10, 20, 30, 40, 50]) == (5, 50)
    assert posicao_maximo([3, 1, 9, 2]) == (3, 9)
    assert posicao_minimo([10, 20, 30, 40, 5]) == (5, 5)
    assert posicao_minimo([7, 2, 9, 1]) == (4, 1)

    # ERROS
    assert posicao_maximo([1, 2, 3, 4]) != (1, 4)
    assert posicao_minimo([4, 5, 6, 7]) != (2, 4)

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
