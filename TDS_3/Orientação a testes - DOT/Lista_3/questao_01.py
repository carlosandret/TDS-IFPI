# 1) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]
from random import randint

def gera_lista(qtd_num, max_valor):
    lista = []
    for i in range(qtd_num):
        x = randint(0, max_valor)
        lista.append(x)
    return lista

def tira_repetido(lista):
    nova_lista = []
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista

def main():
    while True:
        try:            
            numeros = gera_lista(10, 10) 
            numeros_sem_repeticao = tira_repetido(numeros)
            
            print(f"\nLista original: {numeros}")
            print(f"\nLista sem repetição: {numeros_sem_repeticao}")
            break
        except:
            print("ERRO: Entrada inválida, digite apenas números, tente novamente!")
if __name__=='__main__':
    main()