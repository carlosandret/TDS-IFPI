# 14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0. Escrever a lista C modificada.

def zera_negativo(lista):
    lista_copia = lista[:]
    for i in range(len(lista)):
        if lista[i] < 0:
            lista_copia[i] = 0
    return lista_copia

def main():
    lista = []
    c = 0
    print("-----------Digite uma lista de 10 números inteiros.-----------")
    while c < 10:
        c += 1
        try:
            # lista = [-1,-3,-4,-5,6,7,8,9,10]
            valor = int(input("--> "))
            lista.append(valor)
        except:
            c -= 1
            print("\nERRO: Entrada inválida, digite apenas números inteiros!")
    lista_resultado = zera_negativo(lista)
    print(f"\nLista original: {lista}")
    print(f"\nLita modificada: {lista_resultado}")  
    
if __name__=="__main__":
    main()

