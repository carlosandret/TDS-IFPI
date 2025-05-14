# 6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
# programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
# também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
# e quantos faturamentos estão abaixo da média.

# Função que gera uma lista aleatória com uma quantidade especificada de números, com intervalo de 1 a 60
from random import randint
def gera_lista(qtd_num):
    lista = []
    while len(lista) < qtd_num:
        x = randint(1, 60)
        if x not in lista:
            lista.append(x)
    return lista

def calcula_faturamento(lista_qtd, lista_valores):
    faturamentos = []
    for i in range(len(lista_qtd)):
        faturamentos.append(lista_qtd[i] * lista_valores[i])
    return faturamentos

def qtd_abaixo_da_media(lista, media):
    resultado = []
    for i in lista:
        if i < media:
            resultado.append(i)
    return len(resultado)

def media_lista(lista):
    return sum(lista) / len(lista)

def main():
    # ACERTOS
    qtd = [1, 2, 3]
    preco = [10.0, 20.0, 30.0]
    fat = calcula_faturamento(qtd, preco)
    assert fat == [10.0, 40.0, 90.0]

    media = media_lista(fat)
    assert media == 46.666666666666664

    abaixo = qtd_abaixo_da_media(fat, media)
    assert abaixo == 2  # 10.0 e 40.0 estão abaixo da média

    # ACERTOS com valores iguais
    qtd2 = [2, 2, 2]
    preco2 = [5.0, 5.0, 5.0]
    fat2 = calcula_faturamento(qtd2, preco2)
    assert fat2 == [10.0, 10.0, 10.0]
    assert media_lista(fat2) == 10.0
    assert qtd_abaixo_da_media(fat2, 10.0) == 0

    # ACERTOS com inteiros
    qtd3 = [1, 2, 3]
    preco3 = [1, 2, 3]
    assert calcula_faturamento(qtd3, preco3) == [1, 4, 9]
    assert media_lista([1, 4, 9]) == 14 / 3
    assert qtd_abaixo_da_media([1, 4, 9], 14 / 3) == 2

    # ERROS
    assert calcula_faturamento([1, 2], [3, 4]) != [1, 2, 3, 4]
    assert media_lista([10, 20, 30]) != 50
    assert qtd_abaixo_da_media([5, 6, 7], 6) != 3  # apenas dois estão abaixo da média

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
