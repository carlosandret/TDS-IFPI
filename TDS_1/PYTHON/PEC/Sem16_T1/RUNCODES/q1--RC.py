# 01.Faça um programa para ler uma matriz quadrada de ordem n e mostre uma tupla com a posição (linha e coluna) do
# maior e menor elemento. O valor de n é inteiro, positivo e deve ser informados pelo usuário.

from random import randint, seed
seed()


def preenche_matriz(linhas, colunas):
    matriz = []
    for lin in range(linhas):
        linha = []
        for col in range(colunas):
            itens = int(input("").strip())
            linha.append(itens)

        matriz.append(linha)

    return matriz

# def imprime_matriz_indice(matriz):
#     for i_linha in range(len(matriz)):
#         print("|", end="")
#         for i_coluna in range(len(matriz[i_linha])):
#             print(f"{matriz[i_linha][i_coluna]:3d}", end=" ")
#         print("|")

def maior_e_menor_item_matriz(matriz):
    sequencia = []
    for linha in matriz:
        for item in linha:
            sequencia.append(item)
    
    return max(sequencia), min(sequencia)

def indice_maior_item(matriz):
    maior_numero, x = maior_e_menor_item_matriz(matriz)
    for i_linha in range(0, len(matriz)):
        for i_coluna in range(len(matriz[i_linha])):
            item = matriz[i_linha][i_coluna]
            if item == maior_numero:
                resultado = i_linha, i_coluna

    return resultado    

def indice_menor_item(matriz):
    x, menor_numero = maior_e_menor_item_matriz(matriz)
    for i_linha in range(len(matriz)):
        for i_coluna in range(0, len(matriz[i_linha])):
            item = matriz[i_linha][i_coluna]
            if item == menor_numero:
                resultado = i_linha, i_coluna
    return resultado
            

def main():
    linhas = int(input("").strip())
    colunas = linhas
    matriz = preenche_matriz(linhas, colunas)
    
    print(f"{indice_maior_item(matriz)}")
    print(f"{indice_menor_item(matriz)}")
    
    
if __name__=="__main__":
    main()