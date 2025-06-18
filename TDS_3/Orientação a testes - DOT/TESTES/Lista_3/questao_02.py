# 2) Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
# o número de vezes que cada número ocorre na sequência.

def numero_ocorrencias(lista):
    dic = {}
    n_lista = []
    for i in lista:
        
        if type(i) != int:
            return Exception
        if i not in n_lista:
            n_lista.append(i)
            dic[i] += 1
        
        