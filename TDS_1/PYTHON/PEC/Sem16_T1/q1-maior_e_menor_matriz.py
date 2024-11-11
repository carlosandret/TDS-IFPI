# 01.Faça um programa para ler uma matriz quadrada de ordem n e mostre uma tupla com a posição (linha e coluna) do
# maior e menor elemento. O valor de n é inteiro, positivo e deve ser informados pelo usuário.


def vetor(n):
    vetor = []
    for linha in range (n):
        linha = int(input())
        vetor.append(linha)
    return vetor

def matriz(n):
    matriz = []
    for elemento in range (n):
        elemento = vetor(n)
        matriz.append(elemento)
    return matriz

def maior(n, matriz):
    maior = matriz[0] [0]
    posicao_maior = (0, 0)
    for a in range(n):
        for b in range(n):
            if matriz[a][b] > maior:
                maior = matriz[a][b]
                posicao_maior = (a, b)
    return posicao_maior

def menor(n, matriz):
    menor = matriz[0] [0]
    posicao_menor = (0, 0)
    for a in range(n):
        for b in range(n):
            if matriz[a][b] < menor:
                menor = matriz[a][b]
                posicao_menor = (a, b)
    return posicao_menor

def main():
    ordem = int(input("Digite um número/ordem de uma matriz quadrada: "))
    ler_matriz = matriz(ordem)
    print (f"O maior elemento da matriz é {maior(ordem, ler_matriz)}")
    print (f"O menor elemento da mantriz é {menor(ordem, ler_matriz)}")

if __name__=="__main__":
    main()