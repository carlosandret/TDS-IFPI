# 10. Escreva um programa composto de uma função Max e o programa principal como segue:
# a) A função Max recebe como parâmetros de entrada quatro números inteiros e retorna o maior. Se forem iguais retorna qualquer um
# deles;
# b) O programa principal lê 4 séries de 4 números a, b, c, d. Para cada série lida imprime o maior dos quatro números usando a função
# Max.
# c) Retorne o maior das quatro séries lidas

def maximo(n1, n2, n3, n4):
    if not all(isinstance(i, int) for i in [n1, n2, n3, n4]):
        return Exception

    lista = [n1, n2, n3, n4]
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior    

def maior_entre_series(series):
    if not isinstance(series, list) or len(series) != 4:
        return Exception
    if not all(isinstance(valor, int) for valor in series):
        return Exception
    return maximo(series[0], series[1], series[2], series[3])

def main():
    # TESTES UNITÁRIOS DA FUNÇÃO MAXIMO
    assert maximo(1, 2, 3, 4) == 4
    assert maximo(10, 5, 2, 8) == 10
    assert maximo(7, 7, 7, 7) == 7
    assert maximo(-1, -5, -3, -2) == -1
    assert maximo("a", 1, 2, 3) == Exception
    assert maximo(1.5, 2, 3, 4) == Exception

    # TESTES PARA A MAIOR ENTRE SÉRIES
    assert maior_entre_series([10, 20, 15, 8]) == 20
    assert maior_entre_series([7, 7, 7, 7]) == 7
    assert maior_entre_series([1, 2, 3, "a"]) == Exception
    assert maior_entre_series([1, 2, 3]) == Exception
    assert maior_entre_series("1234") == Exception

    # TESTE FINAL COM QUATRO SÉRIES
    serie1 = maximo(1, 2, 3, 4)
    serie2 = maximo(10, 20, 15, 8)
    serie3 = maximo(5, 5, 5, 5)
    serie4 = maximo(-1, -2, -3, -4)

    assert maior_entre_series([serie1, serie2, serie3, serie4]) == 20

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()

