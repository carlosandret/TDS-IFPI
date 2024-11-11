from random import randint, seed
seed()

def preenche_matriz(linhas, colunas):
    matriz = [] #Lista vazia
    for lin in range(linhas):
        linha = [] # Cada linha é uma lista (vetor)
        for col in range(colunas):
            linha.append(randint(1, 50))
            
        # Insere a linha na matriz
        matriz.append(linha)
        
    return matriz

def imprime_matriz(matriz):
    for linha in matriz:
        print("|", end="")
        for elemento in linha:
            print(f"{elemento:3d}", end=" ")
            
        print("|")
        
def imprime_matriz_indice(matriz):
    for i_linha in range(len(matriz)):
        print("|", end="")
        for i_coluna in range(len(matriz[i_linha])):
            print(f"{matriz[i_linha][i_coluna]:3d}", end=" ")
        print("|")



def main():
    linha = int(input(""))
    coluna = int(input(""))
    
    matriz = preenche_matriz(linha, coluna) 
    print(matriz)
    
    print(imprime_matriz_indice(matriz))
    
    
    
    
    
if __name__=="__main__":
    main()