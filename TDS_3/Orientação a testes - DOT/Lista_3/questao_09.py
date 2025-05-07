# 9) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando todas as ocorrências de valores repetidos. Ex: [5, 4, 5, 7, 3, 4] = [7, 3]

def retira_repetido(lista):
    n_lista = []
    for i in lista:
        ocorrencia = 0
        for c in lista:
            if i == c:
                ocorrencia += 1
        if ocorrencia < 2:
            n_lista.append(i)
    return n_lista

def main():
    lista = [5, 4, 5, 7, 3, 4]

    print(retira_repetido(lista))
if __name__=="__main__":
    main()