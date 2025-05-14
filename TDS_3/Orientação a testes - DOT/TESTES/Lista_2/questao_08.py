# 8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
# ocorreu a letra ‘A’.
# OBS: Fazer crítica na entrada do caractere para aceitar somente letras.

# Função que confere quantas vezes a letra foi repetida na lista
def confere_repeticao(lista, letra):
    if not isinstance(lista, list):
        return Exception
    if not isinstance(letra, str) or len(letra) != 1 or not letra.isalpha():
        return Exception
    if not all(isinstance(i, str) and len(i) == 1 and i.isalpha() for i in lista):
        return Exception

    cont = 0
    for i in lista:
        if letra.upper() == i.upper():
            cont += 1
    return cont

def main():
    # Lista correta com letras
    lista = ['A', 'A', 'a', 'B', 'C', 'D', 'E', 'A', 'F', 'G', 'H', 'I', 'J']

    # Testes válidos
    assert confere_repeticao(lista, 'A') == 4
    assert confere_repeticao(lista, 'B') == 1
    assert confere_repeticao(lista, 'Z') == 0
    assert confere_repeticao(lista, 'a') == 4  # Teste com letra minúscula

    # Testes de erro
    assert confere_repeticao("não é lista", 'A') == Exception
    assert confere_repeticao(lista, 5) == Exception
    assert confere_repeticao(lista, 'AA') == Exception
    assert confere_repeticao(lista, '') == Exception
    assert confere_repeticao([1, 2, 3], 'A') == Exception
    assert confere_repeticao(['A', 1, 'B'], 'A') == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
