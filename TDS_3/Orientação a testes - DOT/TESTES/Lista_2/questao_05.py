# 5) Faça um programa que leia duas listas de 10 elementos numéricos cada uma e intercale os
# elementos deste em uma outra lista de 20 elementos.

from random import randint

# Função que gera uma lista aleatória com uma quantidade especificada de números, com intervalo de 1 a 50
def gera_lista(qtd_num):
    lista = []
    while len(lista) < qtd_num:
        x = randint(1, 50)
        if x not in lista:
            lista.append(x)
    return lista

# Função que intercala os itens de duas listas e retorna uma nova lista conjugada 
def intercala_lista(lista_1, lista_2):
    nova_lista = []
    for i in range(len(lista_1)):
        nova_lista.append(lista_1[i])
        nova_lista.append(lista_2[i])
    return nova_lista

def main():
    # ACERTOS – com números
    assert intercala_lista([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]
    assert intercala_lista([10, 20], [30, 40]) == [10, 30, 20, 40]
    assert intercala_lista([], []) == []
    assert intercala_lista([7], [8]) == [7, 8]

    # ACERTOS – com strings
    assert intercala_lista(["a", "b"], ["x", "y"]) == ["a", "x", "b", "y"]
    assert intercala_lista(["dog", "cat"], ["bone", "fish"]) == ["dog", "bone", "cat", "fish"]
    assert intercala_lista([""], [""]) == ["", ""]

    # ERROS – com números
    assert intercala_lista([1, 2], [3, 4]) != [1, 2, 3, 4]
    assert intercala_lista([5, 6], [7, 8]) != [5, 6, 7, 8]

    # ERROS – com strings
    assert intercala_lista(["a", "b"], ["x", "y"]) != ["a", "b", "x", "y"]
    assert intercala_lista(["one", "two"], ["three", "four"]) != ["one", "two", "three", "four"]

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()


