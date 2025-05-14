# 9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
# uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.

# Função que recebe uma lista e retorna a mesma na ordem inversa
def lista_inversa(lista):
    if not isinstance(lista, list):
        return Exception
    if not all(isinstance(i, (int, float)) for i in lista):
        return Exception
    
    lista_invertida = []
    # Loop que percorre a lista e adiciona os valores na ordem inversa em outra lista
    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])    
    return lista_invertida   

def main():
    # Testes com números
    assert lista_inversa([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert lista_inversa([10, 20, 30, 40, 50]) == [50, 40, 30, 20, 10]
    assert lista_inversa([7.1, 2.2, 3.3, 4.4, 5.5]) == [5.5, 4.4, 3.3, 2.2, 7.1]
    assert lista_inversa([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]
    
    # Teste com entrada inválida (lista contendo string)
    assert lista_inversa([1, 2, "3", 4, 5]) == Exception
    assert lista_inversa(["a", "b", "c"]) == Exception
    assert lista_inversa("abcde") == Exception
    assert lista_inversa(12345) == Exception
    assert lista_inversa(None) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
