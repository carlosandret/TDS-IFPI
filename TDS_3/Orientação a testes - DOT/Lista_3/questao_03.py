# 3) Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1] = 25

# Função que gera uma lista de números aletórios, recebe a quantidade de números e o valor maximo da sequência
from random import randint
def gera_lista(qtd_num, max_valor):
    lista = []
    for i in range(qtd_num):
        x = randint(0, max_valor)
        lista.append(x)
    return lista

# Função que recebe uma lista e retorna a maior soma de um segmento de 2 valores
def calc_maior_soma(lista):
    maior_soma = 0
    for i in range(len(lista) - 1):
        soma = lista[i] + lista [i + 1]
        if soma > maior_soma:
            maior_soma = soma            
    return maior_soma
    
def main():
    while True:
        try:            
            lista_original = gera_lista(10, 10)
            maior_soma = calc_maior_soma(lista_original) 

            print(f"\nLista original: {lista_original}")
            print(f"\nMaior de um segmento com dois valores: {maior_soma}")
            break   
        except:
            print("ERRO: Entrada inválida, digite apenas números, tente novamente!")
if __name__=='__main__':
    main()