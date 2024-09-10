# 2. Usando apenas as estruturas básicas de programação, reescreva a funções count(), que recebe
# uma lista e um valor e retorna o número de ocorrências do valor na lista. Por exemplo
# count([1, 2, 3, 2, 4, 2, 5], 2) retorna 3, a quantidade de vezes que o valor 2
# aparece na lista.

def func_count(lista, valor):
    ocorrencias = 0
    for c in lista:
        if c == valor:
            ocorrencias += 1
    return ocorrencias

def main():
    lista_valores = []
    print("")
    while True:
        item = int(input(""))
        if item != 0:
            lista_valores.append(item)
        elif item == 0: break

    valor = int(input(""))
    
    print(f"{lista_valores}")
    print(f"{valor}")
    print(f"{func_count(lista_valores, valor)}")
    
if __name__=="__main__":
    main()