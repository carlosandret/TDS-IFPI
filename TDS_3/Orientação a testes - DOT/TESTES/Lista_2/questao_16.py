#16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3. Escrever as listas X e Y.

# Função que cria uma lista baseada em outra, com uma fórmula para criação de cada elemento
def modifica_lista(lista):
    if type(lista) != list:
        return Exception

    for item in lista:
        if type(item) not in [int, float] or item < 0:
            return Exception

    lista_modificada = []
    for i in range(len(lista)):
        if i % 2 == 0:
            lista_modificada.append(lista[i] / 2)
        else:
            lista_modificada.append(lista[i] * 3)
    return lista_modificada

def main():
    # Testes válidos
    assert modifica_lista([10, 10, 10, 10]) == [5.0, 30, 5.0, 30]
    assert modifica_lista([0, 1, 2, 3]) == [0.0, 3, 1.0, 9]
    assert modifica_lista([1, 2, 3, 4, 5]) == [0.5, 6, 1.5, 12, 2.5]
    assert modifica_lista([2.0, 3.0, 4.0]) == [1.0, 9.0, 2.0]

    # Testes inválidos
    assert modifica_lista("abc") == Exception
    assert modifica_lista([-1, 2, 3]) == Exception
    assert modifica_lista([1, "a", 3]) == Exception
    assert modifica_lista([None, 2, 3]) == Exception
    assert modifica_lista([[], {}, 5]) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()