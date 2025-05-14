# 14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0. Escrever a lista C modificada.

# Função que recebe uma lista e retorna uma cópia, substituindo os valores negativos por zero
def zera_negativo(lista):
    if type(lista) != list:
        return Exception

    for item in lista:
        if type(item) != int:
            return Exception

    lista_copia = lista[:]
    for i in range(len(lista_copia)):
        if lista_copia[i] < 0:
            lista_copia[i] = 0
    return lista_copia

def main():
    # Testes válidos
    assert zera_negativo([1, -2, 3, -4, 5]) == [1, 0, 3, 0, 5]
    assert zera_negativo([-1, -1, -1]) == [0, 0, 0]
    assert zera_negativo([0, 0, 0]) == [0, 0, 0]
    assert zera_negativo([10, 20, 30]) == [10, 20, 30]
    assert zera_negativo([]) == []

    # Testes inválidos
    assert zera_negativo("string") == Exception
    assert zera_negativo(10) == Exception
    assert zera_negativo([1, 2, "a"]) == Exception
    assert zera_negativo([None, 5, -3]) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()