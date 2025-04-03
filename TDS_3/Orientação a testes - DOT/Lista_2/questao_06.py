# 6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
# programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
# também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
# e quantos faturamentos estão abaixo da média.

# Função que gera uma lista aleatória com uma quantidade especificada de números, com intervalo de 1 a 10
from random import randint
def gera_lista(qtd_num):
    lista = []
    while len(lista) < qtd_num:
        x = randint(1, 10)
        if x not in lista:
            lista.append(x)
    return lista

def calcula_faturamento(lista_qtd, lista_valores):
    faturamentos = []
    for i in range(len(lista_qtd)):
        faturamentos.append(lista_qtd[i]*lista_valores[i])
    return faturamentos

def main():
    while True:
        lista_1 = []
        lista_2 = []
        if type(lista_1) and type(lista_2) != str:
            

        else:
            print("Entrada inválida! a lista deve ser de números, tente novamente!")



if __name__=="__main__":
    main()