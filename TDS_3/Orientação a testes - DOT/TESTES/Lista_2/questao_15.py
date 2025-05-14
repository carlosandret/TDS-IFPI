# 15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assimpor diante. Escrever todo a lista D e todo a lista E.

# Função que recebe uma lista e retorna a mesma na ordem inversa
def lista_inversa(lista):
    if type(lista) != list:
        return Exception
    
    for item in lista:
        if type(item) not in [int, float, str]:
            return Exception
    
    lista_invertida = []
    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])
    
    return lista_invertida

def main():
    # Testes válidos com números
    assert lista_inversa([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert lista_inversa([]) == []
    assert lista_inversa([10]) == [10]
    assert lista_inversa([3.1, 2.2, 1.3]) == [1.3, 2.2, 3.1]

    # Testes válidos com strings
    assert lista_inversa(["a", "b", "c"]) == ["c", "b", "a"]
    assert lista_inversa(["um", "dois", "três"]) == ["três", "dois", "um"]

    # Testes inválidos
    assert lista_inversa("string") == Exception
    assert lista_inversa(123) == Exception
    assert lista_inversa([None, "ok"]) == Exception
    assert lista_inversa([[], {}, 1]) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()