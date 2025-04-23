# 2) Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
# o número de vezes que cada número ocorre na sequência.

# Função que gera uma lista de números aletórios, recebe a quantidade de números e o valor maximo da sequência
from random import randint
def gera_lista(qtd_num, max_valor):
    lista = []
    for i in range(qtd_num):
        x = randint(0, max_valor)
        lista.append(x)
    return lista

# Função que retira os itens repetidos da lista, retorna uma nova lista sem repetição
def tira_repetido(lista):
    nova_lista = []
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista

# Função que conta quantas vezes cada item aparece na lista, retorna a quantidade 
def conta_instancia(item, lista):
    cont = 0
    for i in lista:
        if i == item:
            cont += 1
    return cont

# Função que imprime a quantidade de vezes que cada número aparece na lista original
def conta_quantidade_lista(lista_original, numeros):
    for i in numeros:
        qtd = conta_instancia(i, lista_original)
        print(f"O número {i} aparece {qtd}",
        "vez" if qtd == 1 else "vezes")
    
def main():
    while True:
        try:            
            lista_original = gera_lista(10, 10) 
            lista_sem_repeticao = tira_repetido(lista_original)
            
            print(f"\nLista original: {lista_original}\n")
            
            conta_quantidade_lista(lista_original, lista_sem_repeticao)    
            break
        except:
            print("ERRO: Entrada inválida, digite apenas números, tente novamente!")
if __name__=='__main__':
    main()