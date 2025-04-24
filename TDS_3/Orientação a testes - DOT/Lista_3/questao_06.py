# 6) Escreva uma função que recebe uma lista com n números inteiros, e retorna True
# caso a lista esteja ordenada em ordem ascendente ou False caso não esteja
# ordenada. Ex [1, 2, 3] = True. Ex. [3, 7, 2] = False

# Função que gera uma lista de números aletórios, recebe a quantidade de números e o valor maximo da sequência
from random import randint
def gera_lista(qtd_num, max_valor):
    lista = []
    for i in range(qtd_num):
        x = randint(0, max_valor)
        lista.append(x)
    return lista

def confere_crescente(lista):
    cont = 0
    for i in range(len(lista)-1):
        if lista[i+1] > lista[i]:
            cont += 1
    if cont == len(lista)-1:
        return True
    return False
            
def main():
    while True:
        try:            
            # lista_original = gera_lista(5, 20)
            lista_original = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

            print(f"\nLista: {lista_original}")
            print(f"\nLista em ordem crescente? {confere_crescente(lista_original)}")
            
            break   
        except:
            print("ERRO: Entrada inválida, digite apenas números, tente novamente!")
if __name__=='__main__':
    main()