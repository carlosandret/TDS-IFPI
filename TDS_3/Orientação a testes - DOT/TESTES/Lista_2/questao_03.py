# 3) Faça um programa que dada uma sequência de n números, imprimi-la na ordem inversa à da
# leitura.

from random import randint
# Função que gera uma lista aleatória com uma quantidade especificada de números, com intervalo de 1 a 10
def gera_lista(qtd_num):
    lista = []
    while len(lista) < qtd_num:
        x = randint(1, 10)
        if x not in lista:
            lista.append(x)
    return lista

#Função que recebe uma lista e retorna a mesma na ordem inversa
def lista_inversa(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

def main():
    # ACERTOS
    assert lista_inversa([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert lista_inversa([10, 20, 30]) == [30, 20, 10]
    assert lista_inversa([7]) == [7]
    assert lista_inversa([]) == []

    # ERROS
    assert lista_inversa([1, 2, 3]) != [1, 2, 3]
    assert lista_inversa([5, 6, 7]) != [6, 5, 7]

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()