# 5. Faça um programa que leia duas listas de 10 elementos. Crie uma lista que seja a união entre as 2 listas
# anteriores, ou seja, que contêm os números das duas listas. Não deve conter números repetidos.

def recebe_lista(qtd):
    lista = []
    for c in range(qtd):
        item = int(input(""))
        lista.append(item)
    return lista

def retira_repetido(lista):
    for c in range(len(lista)):
        if lista[c] in lista[: c]:
            lista.remove(lista[c])
        
    return lista
    
def main():
    lista1 = recebe_lista(4)
    lista2 = recebe_lista(4)   
    
    lista_uniao = lista1[:]
    for c in range(0, len(lista1)):
        lista_uniao.append(lista2[c])
    
    print(lista_uniao)
    print(f"{retira_repetido(lista_uniao)}")
    
if __name__=="__main__":
    main()