# 1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
# a) Mostre a quantidade de números pares;
# b) Grave uma lista somente com os números pares e mostre a lista;
# c) Mostre a quantidade de números ímpares;
# d) Grave uma lista somente com os números ímpares e mostre a lista.

from random import randint

# Gera uma lista de 'qtd_num' números inteiros únicos entre 1 e 100
def gera_lista(qtd_num):
    if qtd_num > 100:
        return Exception  # Só existem 100 inteiros únicos de 1 a 100
    
    lista = []
    while len(lista) < qtd_num:
        num = randint(1, 100)
        if num not in lista:
            lista.append(num)
    return lista

# Verifica se é par
def eh_par(n):
    return n % 2 == 0

# Separa pares, ímpares e conta quantidades
def qtd_pares_impares(lista_numeros):
    num_pares = []
    num_impares = []
    
    for i in lista_numeros:
        if eh_par(i):
            num_pares.append(i)
        else:
            num_impares.append(i)
    
    qtd_par = len(num_pares)
    qtd_impar = len(num_impares)
    return num_pares, num_impares, qtd_par, qtd_impar

def main():
    # ACERTOS
    lista_teste = [2, 4, 6, 1, 3, 5]
    num_pares, num_impares, qtd_pares, qtd_impares = qtd_pares_impares(lista_teste)
    assert qtd_pares == 3
    assert qtd_impares == 3
    assert num_pares == [2, 4, 6]
    assert num_impares == [1, 3, 5]

    lista = gera_lista(100)
    assert len(lista) == 100
    assert len(lista) == len(set(lista))  # Todos os números devem ser únicos
    
    # ERROS
    assert gera_lista(101) == Exception

    print("Todos os testes passaram!")
if __name__ == "__main__":
    main()