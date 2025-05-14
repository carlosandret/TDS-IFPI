# 17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V aparece. Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto.

# Função que confere quantas vezes o valor foi repetido na lista e retorna posições
def confere_repeticao(lista, valor):
    if type(lista) != list:
        return Exception

    posicoes = []

    for i in range(len(lista)):
        if lista[i] == valor:
            posicoes.append(i)

    return (len(posicoes), posicoes)

def main():
    # Testes válidos
    assert confere_repeticao(["a", "b", "c", "a"], "a") == (2, [0, 3])
    assert confere_repeticao([1, 2, 3, 2, 5], 2) == (2, [1, 3])
    assert confere_repeticao(["x", "y", "z"], "w") == (0, [])
    assert confere_repeticao([], "qualquer") == (0, [])

    # Testes inválidos
    assert confere_repeticao("não é lista", "a") == Exception
    assert confere_repeticao(None, "a") == Exception
    assert confere_repeticao(123, 1) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
