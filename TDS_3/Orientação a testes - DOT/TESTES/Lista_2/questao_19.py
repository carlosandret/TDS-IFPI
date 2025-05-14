# 19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos de S. Escrever a lista X.

# Função que junta duas listas em uma terceira (R com 5 elementos e S com 10)
def concatena_listas(r, s):
    if type(r) != list or type(s) != list:
        return Exception
    if len(r) != 5 or len(s) != 10:
        return Exception
    return r + s

def main():
    # Testes válidos
    assert concatena_listas([1, 2, 3, 4, 5], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == \
           [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    assert concatena_listas(['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']) == \
           ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

    # Testes inválidos
    assert concatena_listas("não é lista", [1]*10) == Exception
    assert concatena_listas([1]*5, "também não é lista") == Exception
    assert concatena_listas([1, 2], [3]*10) == Exception  # Lista R com tamanho incorreto
    assert concatena_listas([1]*5, [2]*5) == Exception    # Lista S com tamanho incorreto
    assert concatena_listas(None, None) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
