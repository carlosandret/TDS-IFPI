# 5. Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir uma lista C de 50 elementos,
# cujos elementos sejam a intercalação dos elementos de A e B.
# Exemplo:

#      0  1  2        23 24
# A = 23 37 30 . . . 38 55
# B = 30 32 46 . . . 43 49
#      0  1  2  3  4  5       46  47  48  49
# C = 23 30 37 32 30 46 . . . 38 43 55 49

# Bom Trabalho!


def main():
    lista_a = []
    for i in range(25):
        elemento = int(input(""))
        lista_a.append(elemento)
        
    lista_b = []
    for i in range(25):
        elemento2 = int(input(""))
        lista_b.append(elemento2)

    # a lista c recebe os termos de a e b de forma intercalada
    lista_c = []
    for x, y in zip(lista_a, lista_b):
        lista_c.append(x)
        lista_c.append(y)
    print(lista_a)
    print(lista_b)
    print(lista_c)
    
if __name__=="__main__":
    main()