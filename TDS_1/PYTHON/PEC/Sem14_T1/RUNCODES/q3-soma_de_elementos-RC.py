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
    lista_a = recebe_valor(20)
    # Lista B    
    lista_b = recebe_valor(20)
    
    soma_dos_termos = soma_listas(lista_a, lista_b)
    
    print(f"{lista_a}")
    print(f"{lista_b}")
    print(f"{soma_dos_termos}")

if __name__=="__main__":
    main()