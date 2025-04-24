# 5) Escreva uma função que recebe uma lista com n números inteiros, e retorna uma
# lista com a soma cumulativa dos elementos da lista original onde o i-ésimo
# elemento é a soma dos primeiros i+1 elementos da lista original. Ex: [1,2,3] = [1,3,6]

# Função que gera uma lista de números aletórios, recebe a quantidade de números e o valor maximo da sequência
from random import randint
def gera_lista(qtd_num, max_valor):
    lista = []
    for i in range(qtd_num):
        x = randint(0, max_valor)
        lista.append(x)
    return lista

# Função que recebe uma lista e retorna uma nova lista contendo a soma dos itens 
def soma_cumulativa(lista):
    nova_lista = []
    for i in range(len(lista)):
        soma = 0
        for c in range(i, -1, -1):
            soma += lista[c]
        nova_lista.append(soma)
    return nova_lista

def main():
    while True:
        try:            
            lista_original = gera_lista(10, 10)
            lista_cumulativa = soma_cumulativa(lista_original)
            
            print(f"\nLista original: {lista_original}")
            print(f"\nLista com elementos somados cumulativamente: {lista_cumulativa}")
            break   
        except:
            print("ERRO: Entrada inválida, digite apenas números, tente novamente!")
    
    
if __name__=="__main__":
    main()