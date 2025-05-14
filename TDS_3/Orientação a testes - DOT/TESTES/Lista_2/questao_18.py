# 18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.

# Função que copia os valores negativos de uma lista para outra separada, retornando a nova lista
def retira_negativos(lista):
    if type(lista) != list:
        return Exception
    
    nova_lista = []
    for i in range(len(lista)):
        if type(lista[i]) not in [int, float]:
            return Exception
        if lista[i] < 0:
            nova_lista.append(lista[i])
    return nova_lista

def main():
    # Testes válidos
    assert retira_negativos([1, -2, 3, -4, 5]) == [-2, -4]
    assert retira_negativos([-1, -2, -3]) == [-1, -2, -3]
    assert retira_negativos([0, 2, 4]) == []
    assert retira_negativos([]) == []

    # Testes inválidos
    assert retira_negativos("não é lista") == Exception
    assert retira_negativos(None) == Exception
    assert retira_negativos([1, "a", 3]) == Exception
    assert retira_negativos([1, 2, [3]]) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
