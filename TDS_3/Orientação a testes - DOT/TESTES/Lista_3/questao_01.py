# 1) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]

def remove_repeticao(lista):
    
    n_lista = []
    for i in lista:
        if type(i) != int:
            return Exception
             
        if i not in n_lista:
            n_lista.append(i)
    return n_lista


assert remove_repeticao([5, 4, 5, 7, 3, 4]) == [5, 4, 7, 3]
assert remove_repeticao(['a', 'b', 'c', 'f']) == Exception
assert remove_repeticao([5, 9, 7, 'c', 'f']) == Exception

