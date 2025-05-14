# 10) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
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
    if not isinstance(lista, list):
        return Exception
    if not all(isinstance(i, (int, float)) for i in lista):
        return Exception
    if len(lista) == 0:
        return Exception
    
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return lista.index(maior) + 1, maior

# Função para encontrar o menor item de uma lista, retorna a posição e o valor do menor item    
def posicao_minimo(lista):
    if not isinstance(lista, list):
        return Exception
    if not all(isinstance(i, (int, float)) for i in lista):
        return Exception
    if len(lista) == 0:
        return Exception

    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return lista.index(menor) + 1, menor

def main():
    # Testes válidos
    lista_1 = [10, 5, 3, 8, 25, 17, 1, 30, 12, 22, 14, 9, 6, 4, 2]
    assert posicao_maximo(lista_1) == (8, 30)
    assert posicao_minimo(lista_1) == (7, 1)

    lista_2 = [100, 99, 98, 97, 96]
    assert posicao_maximo(lista_2) == (1, 100)
    assert posicao_minimo(lista_2) == (5, 96)

    lista_3 = [-5, -10, -3, -50]
    assert posicao_maximo(lista_3) == (3, -3)
    assert posicao_minimo(lista_3) == (4, -50)

    # Testes com erro
    assert posicao_maximo("123") == Exception
    assert posicao_maximo(["a", "b", "c"]) == Exception
    assert posicao_maximo([1, "b", 3]) == Exception
    assert posicao_maximo([]) == Exception

    assert posicao_minimo("xyz") == Exception
    assert posicao_minimo(["x", 1, 2]) == Exception
    assert posicao_minimo([1.2, 3.4, "z"]) == Exception
    assert posicao_minimo([]) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()