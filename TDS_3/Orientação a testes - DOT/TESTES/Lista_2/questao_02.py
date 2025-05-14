# 2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
# de números negativos e a soma dos números positivos dessa lista.

def qtd_negativos(lista):
    qtd = 0
    for i in lista:
        if i < 0:
            qtd += 1
    return qtd

def soma_positivos(lista):
    soma = 0
    for i in lista:
        if i >= 0:
            soma += i
    return soma

def main():
    # ACERTOS
    assert qtd_negativos([1.0, -2.5, 3.2, -4.1, 5.7]) == 2
    assert qtd_negativos([0.0, -1.1, -3.3, 4.4, 5.5]) == 2
    assert qtd_negativos([1, 2, 3, 4, 5]) == 0
    assert soma_positivos([1.0, -2.5, 3.2, -4.1, 5.7]) == 9.9
    assert soma_positivos([-1.0, -2.0, -3.0]) == 0
    assert soma_positivos([0.0, 1.5, 2.5]) == 4.0

    # ERROS
    assert qtd_negativos([]) == 0
    assert soma_positivos([]) == 0

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()