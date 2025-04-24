# 8) Escreva uma função que recebe uma lista com n números inteiros, e retorna o valor
# mais próximo da média de valores da lista. Ex [2.5, 7.5, 10.0, 4.0] = 7.5


# Função que gera uma lista de números aletórios, recebe a quantidade de números e o valor maximo da sequência
from random import randint
def gera_lista(qtd_num, max_valor):
    lista = []
    for i in range(qtd_num):
        x = randint(0, max_valor)
        lista.append(x)
    return lista

def num_proximo_media(lista):
    media = sum(lista) / len(lista)
    valor_mais_proximo = 0
    menor_diferenca = 0
    for i in lista:
        diferenca = media - i
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            valor_mais_proximo = i
            
    return valor_mais_proximo
    
    
    
def main():
    while True:
        try:            
            # lista_original = gera_lista(5, 20)
            lista_original = [1,2,3,4,5]

            print(f"\nLista: {lista_original}")
            print(f"\nO valor mais próximo da média é: {num_proximo_media(lista_original)}")
            break   
        except:
            print("ERRO: Entrada inválida, digite apenas números, tente novamente!")
if __name__=='__main__':
    main()