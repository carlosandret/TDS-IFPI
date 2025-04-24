# 7) Escreva uma função que recebe uma lista com n números inteiros, e retorna True
# caso algum elemento apareça mais de uma vez ou False caso nenhum elemento
# apareça mais de uma vez. Ex [1, 2, 3, 1] = True. Ex. [3, 7, 2, 4] = False

# Função que gera uma lista de números aletórios, recebe a quantidade de números e o valor maximo da sequência
from random import randint
def gera_lista(qtd_num, max_valor):
    lista = []
    for i in range(qtd_num):
        x = randint(0, max_valor)
        lista.append(x)
    return lista

def confere_repeticao(lista):
    l = []
    for i in range(len(lista)):
        if lista[i] in l:
            return True
        else:
            l.append(lista[i])
    return False

def main():
    while True:
        try:            
            # lista_original = gera_lista(5, 20)
            lista_original = [1,2,3,4,5,6,7,8,9,10,11,11,13,14]

            print(f"\nLista: {lista_original}")
            print(f"\nA lista possui item repetido? {confere_repeticao(lista_original)}")
            
            break   
        except:
            print("ERRO: Entrada inválida, digite apenas números, tente novamente!")
if __name__=='__main__':
    main()