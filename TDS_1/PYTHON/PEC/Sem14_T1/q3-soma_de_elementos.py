# 3. Leia duas listas A e B contendo 20 elementos inteiros cada, gerar e exibir uma lista C do mesmo
# tamanho cujos elementos sejam a soma dos respectivos elementos de A e B.

def recebe_valor(qtd):
    lista = []
    for c in range(qtd):
        item = int(input(""))
        lista.append(item)
    return lista

def soma_listas(lista1, lista2):
    lista_resultante = []
    for c in range(0, len(lista1)):
        soma = lista1[c] + lista2[c]
        lista_resultante.append(soma)
        
    return lista_resultante
    
def main():
    # lista A
    print("Digite os termos da primeira lista")
    lista_a = recebe_valor(20)
    # Lista B    
    print("Digite os termos da segunda lista")
    lista_b = recebe_valor(20)
    
    soma_dos_termos = soma_listas(lista_a, lista_b)
    
    print(f"A lista A é: {lista_a}")
    print(f"A lista B é: {lista_b}")
    print(f"A soma dos termos correspondentes da duas listas é: {soma_dos_termos}")

if __name__=="__main__":
    main()