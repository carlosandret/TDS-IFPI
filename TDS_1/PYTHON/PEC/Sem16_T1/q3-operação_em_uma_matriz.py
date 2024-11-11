# 03.Fazer um programa para ler uma matriz n x m de números inteiros. Os valores de n e m são inteiros, positivos e
# devem ser informados pelo usuário, calcular e armazenar em uma tupla para mostrar, respectivamente:
# a) a soma dos elementos da primeira linha
# b) a soma dos elementos da última coluna
# c) a média de todos os elementos
# d) o menor elemento
# e) o maior elemento
# Por exemplo, para a matriz A 4 x 3, abaixo:

# A =

# 0 1 2
# 10 11 12
# 20 21 22
# 30 31 32

# Temos que:
# a) a soma dos elementos da primeira linha é 3
# b) a soma dos elementos da última coluna é 68
# c) a média dos elementos é 16,00
# d) o menor elemento é 0
# e) o maior elemento é 32

# A tupla com a resposta é: (3, 68, 16.00, 0, 32)

def preenche_matriz(linhas, colunas):
    matriz = []
    for lin in range(linhas):
        linha = []
        for col in range(colunas):
            itens = int(input("").strip())
            linha.append(itens)

        matriz.append(linha)
    return matriz

def soma_elementos_linha(linha):
    resutado_soma = 0
    for item in linha:
        resutado_soma += item
    return resutado_soma

def media_elementos_matriz(matriz):
    elementos = []
    for linha in matriz:
        for item in linha:
            elementos.append(item)
    
    return sum(elementos) / len(elementos)

def menor_e_maior_elemento(matriz):
    elementos = []
    for linha in matriz:
        for item in linha:
            elementos.append(item)
    
    return min(elementos), max(elementos)

def main():
    linha = int(input("Digite o número de linhas da matriz: ").strip())
    coluna = int(input("Digite o número de colunas da matriz: ").strip())
    
    matriz = preenche_matriz(linha, coluna)
    
    # a) a soma dos elementos da primeira linha
    soma_primeira_linha = soma_elementos_linha(matriz[0])
    
    # b) a soma dos elementos da última coluna
    resultado_soma = 0
    for i in range(linha):
        resultado_soma += matriz[i][coluna-1]
    
    soma_ultima_coluna = resultado_soma
    
    # c) a média de todos os elementos
    media_elementos = round(media_elementos_matriz(matriz), 4)
    
    # d) o menor elemento
    # e) o maior elemento
    menor, maior = menor_e_maior_elemento(matriz)
    
    resultado = soma_primeira_linha, soma_ultima_coluna, media_elementos, menor, maior 
    print('''A soma dos elementos da primeira linha, a soma dos elementos da última coluna, a média de todos os elementos,
o menor elemento, o maior elemento são: ''')
    print(f"{resultado}")

if __name__=="__main__":
    main()