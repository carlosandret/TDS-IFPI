# 9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos
# no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.

def calcula_soma(n1, n2):
    if not isinstance(n1, int) or not isinstance(n2, int):
        return Exception
    if n1 > n2:
        return Exception
    else:
        soma = 0
        for i in range(n1, n2 + 1):
            soma += i
        return soma

def main():
    # ACERTOS
    assert calcula_soma(1, 5) == 15     # 1+2+3+4+5
    assert calcula_soma(3, 3) == 3      # intervalo de um número só
    assert calcula_soma(-2, 2) == 0     # -2+-1+0+1+2
    assert calcula_soma(0, 0) == 0      # apenas zero

    # ERROS
    assert calcula_soma(5, 1) == Exception
    assert calcula_soma("a", 4) == Exception
    assert calcula_soma(2, "b") == Exception
    assert calcula_soma(None, 2) == Exception
    assert calcula_soma(1.5, 4) == Exception

    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
