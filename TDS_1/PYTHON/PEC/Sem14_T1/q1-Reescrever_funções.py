# As estruturas básicas de programação são sequência, condição e repetição. Usando apenas as
# estruturas básicas de programação, reescreva as funções abaixo (sem utilizá-las):
# a) len(), que recebe uma lista e retorna número de itens;
# b) reverse(), que recebe uma lista e retorna uma lista com os itens na ordem invertida;
# c) min(),que recebe uma lista e retorna o menor valor
# d) max(), que recebe uma lista retorna o maior valor
# e) sum(), que recebe uma lista retorna a soma dos valores


def func_len(lista):
    item = 0
    for c in lista:
        item += 1
    return item

def func_reverse(lista):
    reverso = []
    for c in range(0, func_len(lista)):
        reverso.insert(0, lista[c])
    return reverso

def func_min(lista):
    menor = lista[0]
    for c in range(0, (func_len(lista) - 1)):
        if lista[c + 1] < menor:
            menor = lista[c + 1]
        else:
            continue
    return menor

def func_max(lista):
    maior = lista[0]
    for c in range(0, (func_len(lista) - 1)):
        proximo = lista[c+1]
        if proximo > maior:
            maior = proximo
        else:
            continue
    return maior

def func_sum(lista):
    soma = 0
    for c in lista:
        soma += c
    return soma        
        
def main():
    lista_valores = []
    print("Digite uma lista de valores inteiros:")
    while True:
        item = int(input(""))
        
        if item != 0:
            lista_valores.append(item)
        elif item == 0: break
    print(f"Essa é a sua lista: {lista_valores}")
    print(f"Sua lista possui {func_len(lista_valores)} itens.")
    print(f"A sua lista ao contrário fica assim: {func_reverse(lista_valores)}")
    print(f"O menor item da lista é {func_min(lista_valores)}")
    print(f"O maior item da lista é {func_max(lista_valores)}")
    print(f"A soma dos itens é {func_sum(lista_valores)}")
    
if __name__=="__main__":
    main()